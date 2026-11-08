from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, List
from pydantic import BaseModel
from models.meters import Meter
from models.users import User

class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        # 1. Ищем документ по ID
        doc = await self.get(id)
        if not doc:
            return False
            
        # 2. Получаем только те поля, которые пришли в запросе
        update_data = body.model_dump(exclude_unset=True)
        
        # 3. Обновляем поля прямо в объекте
        for key, value in update_data.items():
            setattr(doc, key, value)
            
        # 4. Сохраняем в базу
        await doc.save()
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

async def initialize_database():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(
        database=client.askue_db,
        document_models=[Meter, User]
    )
