from fastapi import FastAPI
from routes import clients, cards, collections

app = FastAPI()

app.include_router(clients.router)
app.include_router(cards.router)
app.include_router(collections.router)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Simulated Collections API"}
