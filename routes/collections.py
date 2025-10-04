from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException
from database.models.collection import NewCollection
from database.repositories.collection_repository import CollectionRepository
from services.collection_approvement import CollectionApprovement

router = APIRouter(prefix="/cobros", tags=["Collections"])
collection_repository = CollectionRepository()


@router.post("/", response_model=NewCollection)
async def create_collection(collection: NewCollection) -> NewCollection:
    collection.created_at = datetime.now()
    collection_dict = collection.model_dump(exclude_unset=True)
    if await CollectionApprovement().is_valid(collection):
        collection_dict["status"] = "approved"
    else:
        collection_dict["status"] = "declined"
    collection_id = await collection_repository.create(collection_dict)
    collection_dict["id"] = collection_id
    return NewCollection(**collection_dict)


@router.get("/{client_id}", response_model=List[NewCollection])
async def get_collections_by_client_id(client_id: str) -> List[NewCollection]:
    collections = await collection_repository.get_by_client_id(client_id)
    return [NewCollection(**collection) for collection in collections]
