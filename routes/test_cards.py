from fastapi.testclient import TestClient
from main import app
import pytest
from database.repositories.client_repository import ClientRepository
from database.repositories.card_repository import CardRepository

client = TestClient(app)
client_id = "023456789abcdef01234567"
card_id = "123456789abcdef01234567"


@pytest.fixture
def new_card_data():
    return {
        "cliente_id": client_id,
        "pan": "4111111111111111",
        "last4": "5678",
        "bin": "123456",
    }


async def mock_card_repository_create(*args, **kwargs):
    return card_id


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


async def mock_card_repository_get_by_id(*args, **kwargs):
    card_id_arg = args[1]
    if card_id_arg == card_id:
        return {
            "_id": card_id,
            "cliente_id": client_id,
            "pan_masked": "************5678",
            "last4": "5678",
            "bin": "123456",
        }
    return None


async def mock_client_repository_get_by_id_without_result(*args, **kwargs):
    return None


async def mock_updated_card(*args, **kwargs):
    card_id_arg = args[1]
    if card_id_arg == card_id:
        return {
            "_id": card_id,
            "cliente_id": client_id,
            "pan_masked": "************9999",
            "last4": "9999",
            "bin": "654321",
        }
    return None


def test_create_card(new_card_data, monkeypatch):
    monkeypatch.setattr(CardRepository, "create", mock_card_repository_create)
    monkeypatch.setattr(CardRepository, "get_by_id", mock_card_repository_get_by_id)
    monkeypatch.setattr(ClientRepository, "get_by_id", mock_client_repository_get_by_id)
    monkeypatch.setattr(
        CardRepository, "pan_masked_exists", lambda *args, **kwargs: False
    )
    response = client.post("/tarjetas/", json=new_card_data)
    assert response.status_code == 200
    data = response.json()
    assert data["_id"] == card_id
    assert data["cliente_id"] == client_id
    assert data["pan_masked"] == "************5678"
    assert data["last4"] == "5678"
    assert data["bin"] == "123456"


def test_card_create_card_pan_masked_exist(new_card_data, monkeypatch):
    monkeypatch.setattr(CardRepository, "create", mock_card_repository_create)
    monkeypatch.setattr(ClientRepository, "get_by_id", mock_client_repository_get_by_id)
    monkeypatch.setattr(
        CardRepository, "pan_masked_exists", lambda *args, **kwargs: True
    )
    response = client.post("/tarjetas/", json=new_card_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Card with this PAN already exists"}


def test_create_card_with_client_not_found(new_card_data, monkeypatch):
    monkeypatch.setattr(
        ClientRepository, "get_by_id", mock_client_repository_get_by_id_without_result
    )
    response = client.post("/tarjetas/", json=new_card_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Client not found"}


def test_get_card_by_id(monkeypatch):
    monkeypatch.setattr(CardRepository, "get_by_id", mock_card_repository_get_by_id)
    response = client.get(f"/tarjetas/{card_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["_id"] == card_id
    assert data["cliente_id"] == client_id
    assert data["pan_masked"] == "************5678"
    assert data["last4"] == "5678"
    assert data["bin"] == "123456"


def test_get_card_by_id_not_found(monkeypatch):
    monkeypatch.setattr(
        CardRepository, "get_by_id", mock_client_repository_get_by_id_without_result
    )
    response = client.get(f"/tarjetas/{card_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Card not found"}


def test_update_card(monkeypatch):
    monkeypatch.setattr(CardRepository, "update", mock_updated_card)
    monkeypatch.setattr(CardRepository, "get_by_id", mock_card_repository_get_by_id)
    update_resp = client.put(
        f"/tarjetas/{card_id}",
        json={"last4": "9999", "bin": "654321", "cliente_id": client_id},
    )
    assert update_resp.status_code == 200
    data = update_resp.json()
    assert data["pan_masked"] == "************9999"
    assert data["last4"] == "9999"
    assert data["_id"] == card_id
