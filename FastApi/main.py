from fastapi import FastAPI

app = FastAPI()

#creacion de la funcion root
#siempre que se llama a un servidor la operacion que se ejecuta tiene que ser asincrona
@app.get("/")
async def root():
    return "Hello world"

@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}
