from database.repositories.base import BaseRepository
from bson import ObjectId


class CollectionRepository(BaseRepository):
    def __init__(self):
        super().__init__("collections")

    async def get_by_id(self, collection_id: str):
        try:
            obj_id = ObjectId(collection_id)
        except Exception:
            return None
        collection_data = await self.collection.find_one({"_id": obj_id})
        return collection_data

    async def create(self, collection_data: dict):
        result = await self.collection.insert_one(collection_data)
        return str(result.inserted_id)
