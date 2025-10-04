from datetime import datetime
from fastapi import APIRouter, HTTPException
from database.models.collection import NewCollection
from database.repositories.collection_repository import CollectionRepository

router = APIRouter(prefix="/cobros", tags=["Collections"])
collection_repository = CollectionRepository()


@router.post("/")
async def create_collection(collection: NewCollection):
    collection.created_at = datetime.now()
    collection_dict = collection.model_dump(exclude_unset=True)
    collection_id = await collection_repository.create(collection_dict)
    return {"id": collection_id}


@router.get("/client/{client_id}")
async def get_collections_by_client_id(client_id: str):
    collections = await collection_repository.get_by_client_id(client_id)
    return collections
