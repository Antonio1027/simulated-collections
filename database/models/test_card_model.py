from database.models.card import Card, NewCard
from database.models.client import Client


def test_valid_card():
    client = Client(
        id="64b8f0f5e1d3f2a5c6b7d8e7",
        nombre="Model User",
        email="modeluser@example.com",
        telefono="1231231234",
    )
    card = Card(
        cliente_id=client.id, pan_masked="************5678", last4="1234", bin="123456"
    )
    assert card.cliente_id == client.id
    assert card.pan_masked == "************5678"
    assert card.last4 == "1234"
    assert card.bin == "123456"


def test_new_card_and_pan_masked():
    client = Client(
        id="64b8f0f5e1d3f2a5c6b7d8e7",
        nombre="Model User",
        email="modeluser@example.com",
        telefono="1231231234",
    )
    card = NewCard(
        cliente_id=client.id, pan="4111111111115678", last4="5678", bin="123456"
    )
    data = card.model_dump()
    assert data["pan"] == "************5678"
    assert data["last4"] == "5678"
    assert data["bin"] == "123456"
