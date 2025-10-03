from database.repositories.base import BaseRepository
from bson import ObjectId


class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__("clients")

    async def get_by_id(self, client_id: str):
        try:
            obj_id = ObjectId(client_id)
        except Exception:
            return None
        client_data = await self.collection.find_one({"_id": obj_id})
        return client_data

    async def create(self, client_data: dict):
        result = await self.collection.insert_one(client_data)
        return str(result.inserted_id)

    async def update(self, client_id: str, update_data: dict):
        try:
            obj_id = ObjectId(client_id)
        except Exception:
            return None
        await self.collection.update_one({"_id": obj_id}, {"$set": update_data})
        return await self.get_by_id(client_id)

    async def delete(self, client_id: str):
        try:
            obj_id = ObjectId(client_id)
        except Exception:
            return None
        return await self.collection.delete_one({"_id": obj_id})
