from typing import Optional
from sqlmodel import SQLModel, Field

# Таблица для хранения счетчиков АСКУЭ
class Meter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    serial_number: str      # Заводской (серийный) номер
    model_name: str         # Модель счетчика (например, Меркурий 234)
    location: str           # Место установки (например, ТП-15, кв. 42)
    last_reading: float     # Последнее показание (кВт*ч)
    status: str             # Статус (Активен, Отключен, На проверке)

    model_config = {
        "json_schema_extra": {
            "example": {
                "serial_number": "12345678",
                "model_name": "Меркурий 234 ART-03",
                "location": "Подстанция №4, ввод 1",
                "last_reading": 15420.5,
                "status": "Активен"
            }
        }
    }

# Модель для обновления данных счетчика (PUT)
class MeterUpdate(SQLModel):
    serial_number: Optional[str] = None
    model_name: Optional[str] = None
    location: Optional[str] = None
    last_reading: Optional[float] = None
    status: Optional[str] = None
