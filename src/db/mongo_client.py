"""
MongoDB client initialization.
"""

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://admin:admin@localhost:27017/?authSource=admin"
DB_NAME = "adaptive_rag"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
