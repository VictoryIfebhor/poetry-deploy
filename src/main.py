from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"hello": "world"}


@app.get("/{param}")
async def test_param(param: str):
    return {"param": param}
