from database.models.card import NewCard
from database.models.client import Client


def test_valid_card():
    client = Client(
        id="64b8f0f5e1d3f2a5c6b7d8e7",
        nombre="Model User",
        email="modeluser@example.com",
        telefono="1231231234",
    )
    card = NewCard(
        cliente_id=client.id, pan_masked="************1234", last4="1234", bin="123456"
    )
    assert card.cliente_id == client.id
    assert card.pan_masked == "************1234"
    assert card.last4 == "1234"
    assert card.bin == "123456"
