from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/", StaticFiles(directory="web", html=True), name="web")

@app.post("/api/hello")
async def hello(request: Request):
    data = await request.json()
    name = data.get("name", "гість")
    return {"message": f"Привіт, {name}!"}
