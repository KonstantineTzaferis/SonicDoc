from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Smoke test for the API")
async def root(): 
    return {"status": "ok"}






