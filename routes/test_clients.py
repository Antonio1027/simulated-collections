from fastapi.testclient import TestClient
from main import app
import pytest
from database.repositories.client_repository import ClientRepository

client = TestClient(app)
client_id = "023456789abcdef01234567"


@pytest.fixture
def new_client_data():
    return {
        "nombre": "Test Route User",
        "email": "routeuser@example.com",
        "telefono": "9876543210",
    }


async def mock_client_repository_create(*args, **kwargs):
    return client_id


async def mock_client_repository_delete(*args, **kwargs):
    class MockDeleteResult:
        def __init__(self, deleted_count):
            self.deleted_count = deleted_count

    return MockDeleteResult(deleted_count=1)


async def mock_client_repository_get_by_id(*args, **kwargs):
    client_id_arg = args[1]
    if client_id_arg == client_id:
        return {
            "_id": client_id,
            "nombre": "Test Route User",
            "email": "routeuser@example.com",
            "telefono": "9876543210",
        }
    return None


async def mock_updated_client(*args, **kwargs):
    client_id_arg = args[1]
    if client_id_arg == client_id:
        return {
            "_id": client_id,
            "email": "routeuser@example.com",
            "nombre": "Updated Route User",
            "telefono": "1112223333",
        }
    return None


async def mock_delete_not_found(*args, **kwargs):
    class MockDeleteResult:
        def __init__(self, deleted_count):
            self.deleted_count = 0

    return MockDeleteResult(deleted_count=0)


async def mock_is_email_unique(*args, **kwargs):
    return True


async def mock_is_not_email_unique(*args, **kwargs):
    return False


def test_create_client(new_client_data, monkeypatch):
    monkeypatch.setattr(ClientRepository, "create", mock_client_repository_create)
    monkeypatch.setattr(ClientRepository, "is_email_unique", mock_is_email_unique)
    response = client.post("/clientes/", json=new_client_data)
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == new_client_data["nombre"]
    assert data["email"] == new_client_data["email"]
    assert "_id" in data


def test_create_client_duplicate_email(new_client_data, monkeypatch):
    monkeypatch.setattr(ClientRepository, "is_email_unique", mock_is_not_email_unique)
    response = client.post("/clientes/", json=new_client_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already exists"


def test_get_client(monkeypatch):
    monkeypatch.setattr(ClientRepository, "get_by_id", mock_client_repository_get_by_id)
    monkeypatch.setattr(ClientRepository, "is_email_unique", mock_is_email_unique)
    get_resp = client.get(f"/clientes/{client_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["_id"] == client_id
    assert data["nombre"] == data["nombre"]


def test_update_client(monkeypatch):
    monkeypatch.setattr(ClientRepository, "update", mock_updated_client)
    monkeypatch.setattr(ClientRepository, "get_by_id", mock_client_repository_get_by_id)
    update_resp = client.put(
        f"/clientes/{client_id}",
        json={"nombre": "Updated Route User", "telefono": "1112223333"},
    )
    assert update_resp.status_code == 200
    data = update_resp.json()
    assert data["nombre"] == "Updated Route User"
    assert data["telefono"] == "1112223333"
    assert data["_id"] == client_id


def test_delete_client(new_client_data, monkeypatch):
    monkeypatch.setattr(ClientRepository, "create", mock_client_repository_create)
    monkeypatch.setattr(ClientRepository, "delete", mock_client_repository_delete)
    monkeypatch.setattr(ClientRepository, "is_email_unique", mock_is_email_unique)
    create_resp = client.post("/clientes/", json=new_client_data)
    client_id = create_resp.json()["_id"]
    delete_resp = client.delete(f"/clientes/{client_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["message"] == "Client deleted"


def test_delete_client_not_found(monkeypatch):
    monkeypatch.setattr(ClientRepository, "delete", mock_delete_not_found)
    delete_resp = client.delete(f"/clientes/nonexistentid")
    assert delete_resp.status_code == 404
    assert delete_resp.json()["detail"] == "Client not found"
