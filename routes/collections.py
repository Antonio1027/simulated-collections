from fastapi import APIRouter

router = APIRouter(prefix="/cobros", tags=["Cobros"])


@router.get("/")
def get_collections():
    return {"message": "List of collections"}
