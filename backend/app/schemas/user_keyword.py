from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional

class UserKeywordResponse(BaseModel):
    """レスポンスとして返すデータ"""
    id: int
    user_id: int
    keyword_id: int

    class Config:
        from_attributes = True  # SQLAlchemy モデルからの変換を許可