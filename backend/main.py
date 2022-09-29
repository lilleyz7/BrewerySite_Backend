from pyexpat import model
from fastapi import FastAPI, HTTPException

from models import BrewerySave
from fastapi.middleware.cors import CORSMiddleware
from database import (
    fetch_saved_posts,
    save_brewery,
    delete_save
)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/saved")
async def get_saved_brews():
    response = await fetch_saved_posts()
    return response

@app.post("/save", response_model = BrewerySave)
async def save_single_brewery(brewery: BrewerySave):
    response = await save_brewery(dict(brewery))
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.delete("/delete/{name}")
async def delete_by_name(name):
    response = await delete_save(name)
    if response:
        return "successful deletion"
    else:
        raise HTTPException(404, f"There is no save with the name {name}")