from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My first app" 
app.version = "0.0.1"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

# Tags are used to group endpoints in the documentation
@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/movies", tags=['movies'])
def get_movies():
    return movies