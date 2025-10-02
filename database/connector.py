from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# Build the MongoDB URL from environment variables
MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGODB_PORT = os.getenv("MONGODB_PORT", "27017")
MONGODB_DB = os.getenv("MONGODB_DB", "simulated-collections")
MONGODB_USER = os.getenv("MONGODB_USER", "collections")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD", "collpass")

MONGODB_URL = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DB}"

print("Connecting to MongoDB at:", MONGODB_URL)

client = AsyncIOMotorClient(MONGODB_URL)
db = client.get_default_database()