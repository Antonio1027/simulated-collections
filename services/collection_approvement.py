from database.models.collection import NewCollection
from database.repositories.collection_repository import CollectionRepository

CODIGO_MOTIVO_LIST = [
    "01",  # Insufficient funds
    "02",  # Card expired
    "03",  # Invalid card
    "04",  # Suspected fraud
    "05",  # Card blocked
    "06",  # Limit exceeded
    "07",  # Technical error
    "08",  # Duplicate transaction
    "09",  # Invalid amount
]


class CollectionApprovement:
    async def is_valid(self, new_collection: NewCollection) -> bool:
        if new_collection.monto <= 0 or new_collection.monto > 500000.00:
            return False
        if new_collection.codigo_motivo in CODIGO_MOTIVO_LIST:
            return False
        rejected_collections = (
            await CollectionRepository().get_by_status_in_current_month(
                new_collection.tarjeta_id, status="declined"
            )
        )
        if rejected_collections >= 3:
            return False
        return True
