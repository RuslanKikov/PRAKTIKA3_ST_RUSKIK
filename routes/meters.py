from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from typing import List
from models.meters import Meter, MeterUpdate
from database.connection import Database

meter_router = APIRouter(tags=["Счётчики АСКУЭ"])
meter_database = Database(Meter)

@meter_router.post("/new")
async def create_meter(body: Meter) -> dict:
    await meter_database.save(body)
    return {"message": "Счётчик успешно добавлен (Руслан Киков)"}

@meter_router.get("/", response_model=List[Meter])
async def retrieve_all_meters() -> List[Meter]:
    meters = await meter_database.get_all()
    return meters

@meter_router.get("/{id}", response_model=Meter)
async def retrieve_meter(id: PydanticObjectId) -> Meter:
    meter = await meter_database.get(id)
    if not meter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Счётчик с таким ID не найден"
        )
    return meter

@meter_router.put("/{id}", response_model=Meter)
async def update_meter(id: PydanticObjectId, body: MeterUpdate) -> Meter:
    updated_meter = await meter_database.update(id, body)
    if not updated_meter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Счётчик с таким ID не найден"
        )
    return updated_meter

@meter_router.delete("/{id}")
async def delete_meter(id: PydanticObjectId) -> dict:
    meter = await meter_database.delete(id)
    if not meter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Счётчик с таким ID не найден"
        )
    return {"message": "Счётчик удалён из системы"}
