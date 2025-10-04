from pydantic import BaseModel, field_validator
from typing import Optional

from database.models.custom_validators import ClientId, ModelWithObjectId
from database.models.custom_fields import AuditDateTimeFields
from services.card_numbers.validator import CardNumberValidator


class NewCard(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan: str
    last4: str
    bin: str

    @field_validator("pan", mode="before")
    @classmethod
    def validate_pan(cls, v):
        # Accept already masked pan or mask if needed
        if v and len(v) == 16 and v.startswith("************"):
            return v
        if v and len(v) == 16:
            if not CardNumberValidator.validate(v):
                raise ValueError("Invalid card number (Luhn check failed)")
            pan_masked = "************" + v[-4:]
            return pan_masked
        return v


class Card(BaseModel, ModelWithObjectId, AuditDateTimeFields, ClientId):
    pan_masked: Optional[str] = None
    last4: Optional[str] = None
    bin: Optional[str] = None
