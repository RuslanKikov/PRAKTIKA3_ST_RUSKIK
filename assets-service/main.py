from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Assets Service")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.post("/objects/")
def create_object(obj: schemas.ObjectCreate, db: Session = Depends(get_db)):
    # Защита от дубликатов: ищем такой же объект по имени и адресу
    existing = db.query(models.Object).filter(
        models.Object.name == obj.name,
        models.Object.address == obj.address
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Объект с таким названием и адресом уже существует")
        
    new_obj = models.Object(name=obj.name, address=obj.address)
    db.add(new_obj)
    db.commit()
    db.refresh(new_obj)
    return {"id": new_obj.id, "name": new_obj.name, "address": new_obj.address}

@app.get("/objects/")
def get_objects(db: Session = Depends(get_db)):
    return db.query(models.Object).all()

@app.put("/objects/{object_id}")
def update_object(object_id: str, obj_update: schemas.ObjectUpdate, db: Session = Depends(get_db)):
    db_obj = db.query(models.Object).filter(models.Object.id == object_id).first()
    if not db_obj: raise HTTPException(status_code=404, detail="Объект не найден")
    db_obj.name = obj_update.name
    db_obj.address = obj_update.address
    db.commit()
    return {"message": "Данные исправлены", "object": db_obj}

@app.post("/meters/")
def add_meter(meter: schemas.MeterCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Meter).filter(models.Meter.serial_number == meter.serial_number).first()
    if existing: raise HTTPException(status_code=400, detail="Счётчик с таким номером уже существует")
    new_meter = models.Meter(**meter.model_dump())
    db.add(new_meter)
    db.commit()
    return {"id": new_meter.id, "object_id": new_meter.object_id, "serial_number": new_meter.serial_number, "model": new_meter.model}

@app.get("/meters/")
def get_meters(db: Session = Depends(get_db)):
    return db.query(models.Meter).all()
