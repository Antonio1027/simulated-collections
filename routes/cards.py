from fastapi import APIRouter

router = APIRouter(prefix="/tarjetas", tags=["Tarjetas"])

@router.get("/")
def get_cards():
    return {"message": "List of cards"}
