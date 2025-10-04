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
    update_data = {"last4": "8765", "bin": "654321"}
    updated_card = await repo.update(inserted_id, update_data)
    assert updated_card["last4"] == "8765"
    assert updated_card["bin"] == "654321"


@pytest.mark.asyncio
async def test_delete_card():
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
    delete_result = await repo.delete(inserted_id)
    assert delete_result.deleted_count == 1
    card = await repo.get_by_id(inserted_id)
    assert card is None


@pytest.mark.asyncio
async def test_pan_masked_exists():
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
    await repo.create(card_data)
    existing = await repo.pan_masked_exists("************5678")
    assert existing is True
