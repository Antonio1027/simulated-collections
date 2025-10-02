from database.repositories.base import BaseRepository

class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__("clients")

    async def get_by_id(self, client_id: str):
        return await self.collection.find_one({"_id": client_id})

    async def create(self, client_data: dict):
        result = await self.collection.insert_one(client_data)
        return str(result.inserted_id)

    async def update(self, client_id: str, update_data: dict):
        await self.collection.update_one({"_id": client_id}, {"$set": update_data})
        return await self.get_by_id(client_id)

    async def delete(self, client_id: str):
        return await self.collection.delete_one({"_id": client_id})

    async def list_all(self):
        return await self.collection.find().to_list(100)
