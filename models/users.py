from typing import Optional
from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    email: EmailStr
    password: str
    # В методичке тут было поле events: Optional[List[Link[Event]]]
    # Так как у нас тема АСКУЭ, мы можем связать пользователя со счётчиками (опционально)
    # Для простоты оставим просто пустой список строк или вовсе уберем.
    meters: Optional[list[str]] = [] 

    class Settings:
        name = "users"

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Stro0ng!"
            }
        }
    }
