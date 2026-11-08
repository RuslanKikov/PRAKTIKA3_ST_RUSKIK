from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

    model_config = {
        "json_schema_extra": {
            "example": {"id": 1, "item": "Пример задачи от Руслана Кикова"}
        }
    }


class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "example": {"item": "Прочитать следующую главу книги"}
        }
    }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "example": {
                "todos": [
                    {"item": "Пример задачи 1"},
                    {"item": "Пример задачи 2"}
                ]
            }
        }
    }
