from models import BrewerySave
from password import getPassword
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(getPassword())

database = client.BreweryApp
collection = database.SavedBreweries

async def fetch_saved_posts():
    savedBreweries = []
    cursor = collection.find({})
    async for document in cursor:
        savedBreweries.append(BrewerySave(**document))
    return savedBreweries

async def save_brewery(brewery):
    document = brewery
    result = await collection.insert_one(document)
    return document

async def delete_save(name):
    await collection.delete_one({"name": name})
    return True