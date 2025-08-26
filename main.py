from fastapi import FastAPI
import random

app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello Word"}


# 127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatório": random.randint(0,1000)}



