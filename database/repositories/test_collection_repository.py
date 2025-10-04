import pytest
from database.repositories.collection_repository import CollectionRepository
from database.models.mock_db_collection import MockCollection


@pytest.mark.asyncio
async def test_create_and_get_collection():
    mock_collection = MockCollection()
    repo = CollectionRepository()
    repo.collection = mock_collection

    collection_data = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "cliente_id": "64b8f0f5e1d3f2a5c6b7d8e8",
        "tarjeta_id": "123456789abcdef01234567",
        "monto": 100.0,
        "fecha_intento": "2024-06-20T12:00:00Z",
        "status": "pending",
        "codigo_motivo": "00",
        "nombre": "Test Collection",
        "descripcion": "Test Description",
    }
    inserted_id = await repo.create(collection_data)
    collection = await repo.get_by_id(inserted_id)
    assert collection["cliente_id"] == "64b8f0f5e1d3f2a5c6b7d8e8"
    assert collection["tarjeta_id"] == "123456789abcdef01234567"
    assert collection["monto"] == 100.0
    assert collection["status"] == "pending"
    assert collection["nombre"] == "Test Collection"
    assert collection["descripcion"] == "Test Description"


@pytest.mark.asyncio
async def test_get_collections_by_client_id():
    mock_collection = MockCollection()
    repo = CollectionRepository()
    repo.collection = mock_collection

    collection_data_1 = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "cliente_id": "64b8f0f5e1d3f2a5c6b7d8e8",
        "tarjeta_id": "123456789abcdef01234567",
        "monto": 100.0,
        "fecha_intento": "2024-06-20T12:00:00Z",
        "status": "pending",
        "codigo_motivo": "00",
        "nombre": "Test Collection 1",
        "descripcion": "Test Description 1",
    }
    collection_data_2 = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8ea",
        "cliente_id": "64b8f0f5e1d3f2a5c6b7d8e8",
        "tarjeta_id": "abcdef0123456789abcdef01",
        "monto": 200.0,
        "fecha_intento": "2024-06-21T12:00:00Z",
        "status": "approved",
        "codigo_motivo": "00",
        "nombre": "Test Collection 2",
        "descripcion": "Test Description 2",
    }
    await repo.create(collection_data_1)
    await repo.create(collection_data_2)

    collections = await repo.get_by_client_id("64b8f0f5e1d3f2a5c6b7d8e8")
    assert len(collections) == 2
    assert collections[0]["cliente_id"] == "64b8f0f5e1d3f2a5c6b7d8e8"
    assert collections[1]["cliente_id"] == "64b8f0f5e1d3f2a5c6b7d8e8"
