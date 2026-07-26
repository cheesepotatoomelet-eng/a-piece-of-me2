from pydantic import BaseModel, EmailStr
from datetime import datetime

class PersonalityCreate(BaseModel):
    """POST リクエスト時に受け取るデータ"""
    id: int
    personality: str

class PersonalityResponse(BaseModel):
    """レスポンスとして返すデータ"""
    id: int
    personality: str

class Config:
    from_attributes = True  # SQLAlchemy モデルからの変換を許可