import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("DHRUV0712")
client = motor.motor_asyncio.AsyncIOMotorClient(DHRUV0712)
db = client.clothingdb
