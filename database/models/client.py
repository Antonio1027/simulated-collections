from pydantic import BaseModel, EmailStr, Field, field_validator

from database.models.custom_fields import AuditDateTimeFields
from .custom_validators import ClientValidator, ModelWithObjectId
from typing import Optional


class NewClient(BaseModel, ModelWithObjectId, AuditDateTimeFields):
    nombre: str = Field(..., min_length=15)
    email: EmailStr
    telefono: Optional[str] = None

    @field_validator("email", mode="after")
    @classmethod
    def validate_email(cls, email: EmailStr) -> str:
        if ClientValidator.is_email_unique(email, "clients"):
            raise ValueError("El correo electrónico ya está en uso")
        return email


class Client(ModelWithObjectId, BaseModel, AuditDateTimeFields):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
