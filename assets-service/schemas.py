from pydantic import BaseModel

class ObjectCreate(BaseModel):
    name: str
    address: str

class ObjectUpdate(BaseModel):
    name: str
    address: str

class MeterCreate(BaseModel):
    object_id: str
    serial_number: str
    model: str
    tariff_id: str
