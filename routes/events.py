from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from database.connection import get_session
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Events"])

@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message": "Событие успешно создано (Руслан Киков)"}

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Событие с таким ID не найдено (Руслан Киков)"
    )

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        # В Pydantic v2 метод .dict() заменен на .model_dump()
        event_data = new_data.model_dump(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Событие с таким ID не найдено (Руслан Киков)"
    )

@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "Событие успешно удалено (Руслан Киков)"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Событие с таким ID не найдено (Руслан Киков)"
    )
