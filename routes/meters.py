from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from database.connection import get_session
from models.meters import Meter, MeterUpdate
from typing import List

meter_router = APIRouter(tags=["Счётчики АСКУЭ"])

@meter_router.post("/new")
async def create_meter(new_meter: Meter, session=Depends(get_session)) -> dict:
    session.add(new_meter)
    session.commit()
    session.refresh(new_meter)
    return {"message": "Счётчик успешно добавлен в систему (Руслан Киков)"}

@meter_router.get("/", response_model=List[Meter])
async def retrieve_all_meters(session=Depends(get_session)) -> List[Meter]:
    statement = select(Meter)
    meters = session.exec(statement).all()
    return meters

@meter_router.get("/{id}", response_model=Meter)
async def retrieve_meter(id: int, session=Depends(get_session)) -> Meter:
    meter = session.get(Meter, id)
    if meter:
        return meter
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Счётчик с таким ID не найден"
    )

@meter_router.put("/edit/{id}", response_model=Meter)
async def update_meter(id: int, new_data: MeterUpdate, session=Depends(get_session)) -> Meter:
    meter = session.get(Meter, id)
    if meter:
        meter_data = new_data.model_dump(exclude_unset=True)
        for key, value in meter_data.items():
            setattr(meter, key, value)
        session.add(meter)
        session.commit()
        session.refresh(meter)
        return meter
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Счётчик с таким ID не найден"
    )

@meter_router.delete("/delete/{id}")
async def delete_meter(id: int, session=Depends(get_session)) -> dict:
    meter = session.get(Meter, id)
    if meter:
        session.delete(meter)
        session.commit()
        return {"message": "Счётчик удалён из системы"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Счётчик с таким ID не найден"
    )
