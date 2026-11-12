from sqlalchemy import Column, String
import uuid
from database import Base

class Object(Base):
    __tablename__ = "objects"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    address = Column(String) # НОВОЕ ПОЛЕ

class Meter(Base):
    __tablename__ = "meters"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    object_id = Column(String, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    model = Column(String)
    tariff_id = Column(String)
