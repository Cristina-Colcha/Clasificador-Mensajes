from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
from clasificador import clasificar_mensajes

app = FastAPI()

class Entrada(BaseModel):
    frases: Union[str, List[str]]

@app.post("/clasificar/")
def clasificar(entrada: Entrada):
    return clasificar_mensajes(entrada.frases)
