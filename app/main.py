from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Smoke test for the API")
async def root(): 
    return {"status": "ok"}

@app.get("/hello/{name}", summary="Greet the user by name")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}