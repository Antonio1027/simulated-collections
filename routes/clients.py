from fastapi import APIRouter, HTTPException
from database.models.client import Client, NewClient
from datetime import datetime
from database.repositories.client_repository import ClientRepository

router = APIRouter(prefix="/clientes", tags=["Clientes"])
client_repository = ClientRepository()


@router.post("/", response_model=NewClient)
async def create_client(client: NewClient):
    client.created_at = datetime.now()
    client.updated_at = datetime.now()
    client_dict = client.model_dump(exclude_unset=True)
    client_id = await client_repository.create(client_dict)
    client.id = str(client_id)
    return client


@router.get("/{id}", response_model=Client)
async def get_client(id: str):
    client = await client_repository.get_by_id(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**client)


@router.put("/{id}", response_model=Client)
async def update_client(id: str, client_update: Client):
    update_data = client_update.model_dump(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    updated_client = await client_repository.update(id, update_data)
    if not updated_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**updated_client)


@router.delete("/{id}")
async def delete_client(id: str):
    result = await client_repository.delete(id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted"}
