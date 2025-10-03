from pydantic import BaseModel, EmailStr, Field

from database.models.custom_fields import AuditDateTimeFields
from .custom_validators import ModelWithObjectId
from typing import Optional


class NewClient(BaseModel, ModelWithObjectId, AuditDateTimeFields):
    nombre: str = Field(..., min_length=15)
    email: EmailStr
    telefono: Optional[str] = None


class Client(ModelWithObjectId, BaseModel, AuditDateTimeFields):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
