
from fastapi import FastAPI, HTTPException
import random
import requests
import os

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello Word"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatório": random.randint(0,1000)}


API_KEY = os.getenv("OPENWEATHER_API_KEY")
@app.get("/clima/{cidade}")
async def obter_clima(cidade: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            "cidade": dados["name"],
            "temperatura": dados["main"]["temp"],
            "descricao": dados["weather"][0]["description"],
            "umidade": dados["main"]["humidity"]
        }
        return clima
    else:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
