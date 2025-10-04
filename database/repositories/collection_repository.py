from bson import ObjectId
from database.repositories.base import BaseRepository
from datetime import datetime


class CollectionRepository(BaseRepository):
    def __init__(self):
        super().__init__("collections")

    async def get_by_id(self, collection_id: str):
        try:
            object_id = ObjectId(collection_id)
        except Exception:
            return None
        collection_data = await self.collection.find_one({"_id": object_id})
        return collection_data

    async def create(self, collection_data: dict):
        result = await self.collection.insert_one(collection_data)
        return str(result.inserted_id)

    async def get_by_client_id(self, client_id: str):
        result = self.collection.find({"cliente_id": client_id})
        collections = []
        async for doc in result:
            collections.append(doc)
        return collections

    async def get_by_status_in_current_month(self, tarjeta_id: str, status: str):
        start_of_month = datetime.now().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
        result = self.collection.find(
            {
                "tarjeta_id": tarjeta_id,
                "status": status,
                "created_at": {"$gte": start_of_month},
            }
        )
        collections = []
        async for doc in result:
            collections.append(doc)
        return len(collections)

    async def update(self, collection_id: str, update_data: dict):
        try:
            object_id = ObjectId(collection_id)
        except Exception:
            return None
        await self.collection.update_one({"_id": object_id}, {"$set": update_data})
        return await self.get_by_id(collection_id)
