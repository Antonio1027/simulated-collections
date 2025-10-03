from pydantic import BaseModel, Field

from database.models.custom_validators import ClientId, ModelWithObjectId
from database.models.custom_fields import AuditDateTimeFields


class NewCard(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan_masked: str
    last4: str
    bin: str
