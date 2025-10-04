from database.repositories.base import BaseRepository
from bson import ObjectId


class CardRepository(BaseRepository):
    def __init__(self):
        super().__init__("cards")

    async def get_by_id(self, card_id: str):
        try:
            obj_id = ObjectId(card_id)
        except Exception:
            return None
        card_data = await self.collection.find_one({"_id": obj_id})
        return card_data

    async def create(self, card_data: dict):
        result = await self.collection.insert_one(card_data)
        return str(result.inserted_id)

    async def update(self, card_id: str, update_data: dict):
        try:
            obj_id = ObjectId(card_id)
        except Exception:
            return None
        await self.collection.update_one({"_id": obj_id}, {"$set": update_data})
        return await self.get_by_id(obj_id)

    async def delete(self, card_id: str):
        try:
            obj_id = ObjectId(card_id)
        except Exception:
            return None
        return await self.collection.delete_one({"_id": obj_id})

    async def pan_masked_exists(self, pan_masked: str) -> bool:
        doc = await self.collection.find_one({"pan_masked": pan_masked})
        return doc is not None
