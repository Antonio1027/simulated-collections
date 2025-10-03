from bson import ObjectId
from typing import Optional
from pydantic import Field, field_validator


class ModelWithObjectId:
    id: Optional[str] = Field(default=None, alias="_id")

    @field_validator("id", mode="before")
    @classmethod
    def validate_object_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v


class ClientValidator:
    @classmethod
    async def is_email_unique(cls, email: str, collection) -> bool:
        existing = await collection.find_one({"email": email})
        return existing is None
