from datetime import datetime
from typing import Optional
from pydantic import Field


class AuditDateTimeFields:
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
