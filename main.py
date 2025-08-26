from fastapi import FastAPI

app = FastAPI()


@app.get("/helloword")
async def root():
    return {"message": "Hello Word"}



@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}

