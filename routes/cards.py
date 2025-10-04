from fastapi import APIRouter, HTTPException
from database.models.card import NewCard, Card
from database.repositories.card_repository import CardRepository
from database.repositories.client_repository import ClientRepository
from datetime import datetime

router = APIRouter(prefix="/tarjetas", tags=["Cards"])
card_repository = CardRepository()
client_repository = ClientRepository()


@router.post("/", response_model=Card)
async def create_card(card: NewCard) -> Card:
    card.created_at = datetime.now()
    client = await client_repository.get_by_id(card.cliente_id)
    if not client:
        raise HTTPException(status_code=400, detail="Client not found")
    card_dict = card.model_dump(exclude_unset=True)
    card_dict["pan_masked"] = card_dict.pop("pan")
    existing = card_repository.pan_masked_exists(card_dict["pan_masked"])
    if existing:
        raise HTTPException(status_code=400, detail="Card with this PAN already exists")
    card_id = await card_repository.create(card_dict)
    card.id = card_id
    card = await card_repository.get_by_id(card_id)
    return Card(**card)


@router.get("/{id}", response_model=Card)
async def get_card_by_id(id: str) -> Card:
    card = await card_repository.get_by_id(id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return Card(**card)


@router.put("/{id}", response_model=Card)
async def update_card(id: str, card_update: Card) -> Card:
    card_update.updated_at = datetime.now()
    update_data = card_update.model_dump(exclude_unset=True)
    updated_card = await card_repository.update(id, update_data)
    if not updated_card:
        raise HTTPException(status_code=404, detail="Card not found")
    return Card(**updated_card)


@router.delete("/{id}")
async def delete_card(id: str):
    result = await card_repository.delete(id)
    if not result or (hasattr(result, "deleted_count") and result.deleted_count == 0):
        raise HTTPException(status_code=404, detail="Card not found")
    return {"message": "Card deleted"}
