from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional

class User_personalityResponse(BaseModel):
    """レスポンスとして返すデータ"""
    id: int
    user_id: int
    personality_id: int

    class Config:
        from_attributes = True  # SQLAlchemy モデルからの変換を許可