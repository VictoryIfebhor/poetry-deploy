"""
Main entry point for the application.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    """Index route"""
    return {"hello": "world"}


@app.get("/{param}")
async def test_param(param: str):
    """This tests that params are passed correctly"""
    return {"param": param}
