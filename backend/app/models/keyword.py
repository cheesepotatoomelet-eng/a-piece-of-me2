from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Keywords(Base):
    __tablename__ = "keywords"

    id         = Column(Integer, primary_key=True, index=True)
    keywords   = Column(String, nullable=False)