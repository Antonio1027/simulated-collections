from fastapi import APIRouter, HTTPException
from database.models.card import NewCard, Card
from database.repositories.card_repository import CardRepository
from database.repositories.client_repository import ClientRepository

router = APIRouter(prefix="/tarjetas", tags=["Cards"])
card_repository = CardRepository()
client_repository = ClientRepository()


@router.post("/", response_model=NewCard)
async def create_card(card: NewCard) -> NewCard:
    client = await client_repository.get_by_id(card.cliente_id)
    if not client:
        raise HTTPException(status_code=400, detail="Client not found")
    card_dict = card.model_dump(exclude_unset=True)
    card_id = await card_repository.create(card_dict)
    card.id = card_id
    return card


@router.get("/{id}", response_model=Card)
async def get_card_by_id(id: str) -> Card:
    card = await card_repository.get_by_id(id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return Card(**card)


@router.put("/{id}", response_model=Card)
async def update_card(id: str, card_update: Card) -> Card:
    update_data = card_update.model_dump(exclude_unset=True)
    updated_card = await card_repository.update(id, update_data)
    if not updated_card:
        raise HTTPException(status_code=404, detail="Card not found")
    return Card(**updated_card)
