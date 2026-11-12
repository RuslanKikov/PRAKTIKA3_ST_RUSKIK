from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
import uuid
from database import Base

class Reading(Base):
    __tablename__ = "readings"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    meter_id = Column(String, nullable=False) # Логическая ссылка на assets-service
    value = Column(Float, nullable=False)
    reading_date = Column(DateTime, nullable=False)
    source = Column(String, default="MANUAL")
    status = Column(String, default="ACCEPTED")
    created_at = Column(DateTime, default=datetime.utcnow)
