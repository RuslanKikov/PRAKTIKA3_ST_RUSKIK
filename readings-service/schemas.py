from pydantic import BaseModel
from datetime import datetime

class ReadingCreate(BaseModel):
    meter_id: str
    value: float
    reading_date: datetime
    source: str = "MANUAL"

class ReadingUpdate(BaseModel):
    value: float
    reading_date: datetime
