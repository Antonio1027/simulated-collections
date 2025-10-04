from bson import ObjectId
from database.repositories.base import BaseRepository


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
