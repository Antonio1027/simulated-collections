from fastapi import APIRouter, HTTPException
from database.models.collection import NewCollection
from database.repositories.collection_repository import CollectionRepository

router = APIRouter(prefix="/cobros", tags=["Collections"])
collection_repository = CollectionRepository()


@router.post("/")
async def create_collection(collection: NewCollection):
    collection_dict = collection.model_dump(exclude_unset=True)
    collection_id = await collection_repository.create(collection_dict)
    return {"id": collection_id}
