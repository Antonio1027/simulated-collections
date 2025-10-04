from fastapi.testclient import TestClient
from main import app
import pytest
from database.repositories.collection_repository import CollectionRepository

client = TestClient(app)
client_id = "64b8f0f5e1d3f2a5c6b7d8e8"
collection_id = "64b8f0f5e1d3f2a5c6b7d8e9"


@pytest.fixture
def new_collection_data():
    return {
        "_id": collection_id,
        "cliente_id": client_id,
        "tarjeta_id": "123456789abcdef01234567",
        "monto": 100.0,
        "fecha_intento": "2024-06-20T12:00:00Z",
        "status": "pending",
        "codigo_motivo": "00",
        "nombre": "Test Collection",
        "descripcion": "Test Description",
    }


async def mock_collection_repository_create(*args, **kwargs):
    return collection_id


async def mock_collection_repository_get_by_id(*args, **kwargs):
    collection_id_arg = args[1]
    if collection_id_arg == collection_id:
        return {
            "_id": collection_id,
            "cliente_id": client_id,
            "tarjeta_id": "123456789abcdef01234567",
            "monto": 100.0,
            "fecha_intento": "2024-06-20T12:00:00Z",
            "status": "pending",
            "codigo_motivo": "00",
            "nombre": "Test Collection",
            "descripcion": "Test Description",
        }
    return None


async def mock_collections_by_client_id(*args, **kwargs):
    client_id_arg = args[1]
    if client_id_arg == client_id:
        return [
            {
                "_id": collection_id,
                "cliente_id": client_id,
                "tarjeta_id": "123456789abcdef01234567",
                "monto": 100.0,
                "fecha_intento": "2024-06-20T12:00:00Z",
                "status": "pending",
                "codigo_motivo": "00",
                "nombre": "Test Collection",
                "descripcion": "Test Description",
            }
        ]
    return []


def test_create_collection(new_collection_data, monkeypatch):
    monkeypatch.setattr(
        CollectionRepository, "create", mock_collection_repository_create
    )
    response = client.post("/cobros/", json=new_collection_data)
    assert response.status_code == 200


def test_get_collections_by_client_id(monkeypatch):
    monkeypatch.setattr(
        CollectionRepository, "get_by_client_id", mock_collections_by_client_id
    )
    response = client.get(f"/cobros/{client_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
