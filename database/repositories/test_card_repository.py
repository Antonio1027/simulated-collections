import pytest
from database.repositories.card_repository import CardRepository
from database.models.mock_db_collection import MockCollection


@pytest.mark.asyncio
async def test_create_and_get_card():
    mock_collection = MockCollection()
    repo = CardRepository()
    repo.collection = mock_collection

    card_data = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "cliente_id": "64b8f0f5e1d3f2a5c6b7d8e8",
        "pan_masked": "************5678",
        "last4": "5678",
        "bin": "123456",
    }
    inserted_id = await repo.create(card_data)
    card = await repo.get_by_id(inserted_id)
    assert card["cliente_id"] == "64b8f0f5e1d3f2a5c6b7d8e8"
    assert card["pan_masked"] == "************5678"
    assert card["last4"] == "5678"
    assert card["bin"] == "123456"


@pytest.mark.asyncio
async def test_update_card():
    mock_collection = MockCollection()
    repo = CardRepository()
    repo.collection = mock_collection

    card_data = {
        "_id": "64b8f0f5e1d3f2a5c6b7d8e9",
        "cliente_id": "64b8f0f5e1d3f2a5c6b7d8e8",
        "pan_masked": "************5678",
        "last4": "5678",
        "bin": "123456",
    }
    inserted_id = await repo.create(card_data)
    update_data = {"pan_masked": "************8765"}
    updated_card = await repo.update(inserted_id, update_data)
    assert updated_card["pan_masked"] == "************8765"
