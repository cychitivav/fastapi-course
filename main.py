from fastapi import FastAPI

app = FastAPI()
app.title = "My first app" 
app.version = "0.0.1"

# Tags are used to group endpoints in the documentation
@app.get("/", tags=['home'])
def read_root():
    return {"Hello": "World"}