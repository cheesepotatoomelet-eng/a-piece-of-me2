from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User_keyword(Base):
    __tablename__ = "user_keywords"

    id            = Column(Integer, primary_key=True, index=True)
    user_id       = Column(Integer, ForeignKey("users.id"), nullable=False)
    keyword_id    = Column(Integer, ForeignKey("keywords.id"), nullable=False)