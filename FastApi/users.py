from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

#Entidad user
class User(BaseModel):
    name: str
    lastName: str
    url: str
    age: int

Users_db = [User("Alfredo", "Cano", "https://www.google.com", "27")]

@app.get("/usersjson")
async def usersjson():
    return [
        {"name": "Alfredo", "lastName": "Cano", "url":"https://www.google.com" },
        {"name": "Jose", "lastName": "Hernandez", "url":"https://www.google.com"},
        {"name": "Pedro", "lastName": "Lopez", "url":"https://www.google.com"}
        ]
