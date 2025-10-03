import pytest
from database.models.client import Client, NewClient
from pydantic import ValidationError


def test_valid_client():
    client = Client(
        nombre="Model User", email="model@example.com", telefono="1231231234"
    )
    assert client.nombre == "Model User"
    assert client.email == "model@example.com"
    assert client.telefono == "1231231234"


def test_invalid_email():
    with pytest.raises(ValidationError):
        Client(nombre="Model User", email="not-an-email", telefono="1231231234")


@pytest.mark.asyncio
async def test_missing_nombre():
    with pytest.raises(ValidationError):
        await NewClient.model_validate_json(
            {"email": "model@example.com", "telefono": "1231231234"}
        )


@pytest.mark.asyncio
async def test_missing_email():
    with pytest.raises(ValidationError):
        await NewClient.model_validate_json(
            {"nombre": "Model User", "telefono": "1231231234"}
        )
