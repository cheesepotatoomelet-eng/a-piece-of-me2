from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Connections(Base):
    __tablename__ = "connections"

    id                 = Column(Integer, primary_key=True, index=True)
    keyword_id         = Column(Integer, ForeignKey("keywords.id"), nullable=False)
    personalitie_id    = Column(Integer, ForeignKey("personalities.id"), nullable=False)