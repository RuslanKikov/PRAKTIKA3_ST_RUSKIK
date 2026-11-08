from typing import Optional
from beanie import Document
from pydantic import BaseModel

class Meter(Document):
    serial_number: str
    model_name: str
    location: str
    last_reading: float
    status: str

    class Settings:
        name = "meters"

    model_config = {
        "json_schema_extra": {
            "example": {
                "serial_number": "12345678",
                "model_name": "Меркурий 234",
                "location": "Подстанция №4",
                "last_reading": 15420.5,
                "status": "Активен"
            }
        }
    }

# ВНИМАНИЕ: Здесь мы используем BaseModel, а не Document!
class MeterUpdate(BaseModel):
    serial_number: Optional[str] = None
    model_name: Optional[str] = None
    location: Optional[str] = None
    last_reading: Optional[float] = None
    status: Optional[str] = None
