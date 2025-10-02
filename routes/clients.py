from fastapi import APIRouter

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def get_clients():
    return {"message": "List of clients"}
