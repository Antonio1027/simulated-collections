from fastapi import APIRouter, HTTPException
from database.models.client import Client
from datetime import datetime
from database.repositories.client_repository import ClientRepository

router = APIRouter(prefix="/clientes", tags=["Clientes"])
client_repository = ClientRepository()

@router.post("/", response_model=Client)
async def create_client(client: Client):
    client.created_at = datetime.now()
    client.updated_at = datetime.now()
    client_dict = client.dict(exclude_unset=True)
    client_id = await client_repository.create(client_dict)
    client._id = client_id
    return client

@router.get("/{id}", response_model=Client)
async def get_client(id: str):
    client = await client_repository.get_by_id(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**client)

