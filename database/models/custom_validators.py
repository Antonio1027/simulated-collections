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
