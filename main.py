from fastapi import FastAPI, Body, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"
    },
	{
		"id": 2,
		"title": "Titanic",
		"overview": "Un joven artista se gana la vida pintando retratos de pasajeros ...",
		"year": 1997,
		"rating": 7.8,
		"category": "Drama"
	},
	{
		"id": 3,
		"title": "The Avengers",
		"overview": "Los Vengadores y sus aliados deberán estar dispuestos a sacrificarlo todo ...",
		"year": 2012,
		"rating": 8.1,
		"category": "Acción"
	},
]

# Pydantic models are used to validate the data that is passed to the endpoint
class Movie(BaseModel):
	id: int | None
	title: str = Field(default="", min_length=3, max_length=15)
	overview: str
	year: int = Field(default=2022, ge=2000, le=2023)
	rating: float
	category: str

	class Config:
		schema_extra = {
			"example": {
				"id": 1,
				"title": "Avatar",
				"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
				"year": 2009,
				"rating": 7.8,
				"category": "Acción"
			}
		}

app = FastAPI()
app.title = "My first app"
app.version = "0.0.1"
app.description = "This is my first app with FastAPI"

# Tags are used to group endpoints in the documentation
@app.get("/", tags=['home'])
def message():
	return HTMLResponse('<h1>Hello World</h1>')


@app.get("/movies", tags=['movies'])
def get_movies():
    return movies


# Path parameters are used to pass data to the endpoint
@app.get("/movies/{id}", tags=['movies'])
def get_movie(id: int = Path(le=200, ge=1)):
    for movie in movies:
        if movie['id'] == id:
            return movie

    return {}


# Query parameters are used to pass data to the endpoint
@app.get("/movies/search/", tags=['movies'])
def get_movie_by_category(category: str):
	return list(filter(lambda x: x['category'] == category, movies))


@app.post('/movies', tags=['movies'])
def add_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })

    return movies


@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
	for movie in movies:
		if movie['id'] == id:
			movie['title'] = title
			movie['overview'] = overview
			movie['year'] = year
			movie['rating'] = rating
			movie['category'] = category

	return movies


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
	for movie in movies:
		if movie['id'] == id:
			movies.remove(movie)

	return movies


@app.post('/movies/pydantic', tags=['movies'])
def add_movie_pydantic(movie: Movie):
	movies.append(movie.dict())

	return movies