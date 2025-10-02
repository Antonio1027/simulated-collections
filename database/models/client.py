from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class Client(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nombre: str
    email: EmailStr
    telefono: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
