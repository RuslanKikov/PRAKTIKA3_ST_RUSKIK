from typing import Optional, List
from sqlmodel import JSON, SQLModel, Field, Column

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Презентация книги FastAPI от Руслана Кикова",
                "image": "https://linktomymage.com/image.png",
                "description": "Обсудим книгу FastAPI.",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }
    }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Обновленное название от Руслана",
                "location": "Москва"
            }
        }
    }
