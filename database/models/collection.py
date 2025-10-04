from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from database.models.custom_validators import ModelWithObjectId, ClientId
from database.models.custom_fields import AuditDateTimeFields


class NewCollection(BaseModel, ModelWithObjectId, ClientId, AuditDateTimeFields):
    tarjeta_id: str
    monto: float
    fecha_intento: datetime
    status: Optional[str] = None
    codigo_motivo: str
    reembolsado: Optional[bool] = None
    fecha_reembolso: Optional[str] = None
    nombre: str
    descripcion: Optional[str]
