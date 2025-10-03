from pydantic import BaseModel, Field
from typing import Optional

from database.models.custom_validators import ClientId, ModelWithObjectId
from database.models.custom_fields import AuditDateTimeFields


class NewCard(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan_masked: str
    last4: str
    bin: str


class Card(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan_masked: Optional[str] = None
    last4: Optional[str] = None
    bin: Optional[str] = None
