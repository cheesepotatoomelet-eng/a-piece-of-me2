from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Personality(Base):
    __tablename__ = "personalities"

    id                 = Column(Integer, primary_key=True, index=True)
    personality      = Column(String, nullable=False)