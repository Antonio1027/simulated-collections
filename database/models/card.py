from pydantic import BaseModel, Field, field_validator
from typing import Optional

from database.models.custom_validators import ClientId, ModelWithObjectId
from database.models.custom_fields import AuditDateTimeFields


class NewCard(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan: str
    last4: str
    bin: str

    @field_validator("pan", mode="before")
    @classmethod
    def validate_pan(cls, v):

        if v and len(v) >= 4:
            pan_masked = "************" + v[-4:]
            return pan_masked
        return v


class Card(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan_masked: Optional[str] = None
    last4: Optional[str] = None
    bin: Optional[str] = None
