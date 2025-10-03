import pytest
from database.repositories.client_repository import ClientRepository
from database.models.mock_db_collection import MockCollection


@pytest.mark.asyncio
async def test_create_and_get_client():
    mock_collection = MockCollection()
    repo = ClientRepository()
    repo.collection = mock_collection

    client_data = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "nombre": "Repo User",
        "email": "repo@example.com",
        "telefono": "5555555555",
    }
    inserted_id = await repo.create(client_data)
    client = await repo.get_by_id(inserted_id)
    assert client["nombre"] == "Repo User"
    assert client["email"] == "repo@example.com"
    assert client["telefono"] == "5555555555"


@pytest.mark.asyncio
async def test_update_client():
    mock_collection = MockCollection()
    repo = ClientRepository()
    repo.collection = mock_collection

    client_data = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "nombre": "Repo User",
        "email": "repo2@example.com",
        "telefono": "5555555555",
    }
    await repo.create(client_data)
    update_data = {"nombre": "Updated Repo User"}
    updated_client = await repo.update("64b8f0f5e1d3f2a5c6b7d8e9", update_data)
    assert updated_client["nombre"] == "Updated Repo User"


@pytest.mark.asyncio
async def test_delete_client():
    mock_collection = MockCollection()
    repo = ClientRepository()
    repo.collection = mock_collection

    client_data = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "nombre": "Repo User",
        "email": "repo3@example.com",
        "telefono": "5555555555",
    }
    await repo.create(client_data)
    result = await repo.delete("64b8f0f5e1d3f2a5c6b7d8e9")
    assert result.deleted_count == 1
    deleted_client = await repo.get_by_id("64b8f0f5e1d3f2a5c6b7d8e9")
    assert deleted_client is None
