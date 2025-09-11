import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable not set!")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.clothingdb

