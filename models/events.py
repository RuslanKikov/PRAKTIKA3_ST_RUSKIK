from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Презентация книги FastAPI от Руслана Кикова",
                "image": "https://linktomimage.com/image.png",
                "description": "Обсудим книгу и разберем примеры.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
    }
