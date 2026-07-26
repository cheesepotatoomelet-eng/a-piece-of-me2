from pydantic import BaseModel, EmailStr
from datetime import datetime

class KeywordCreate(BaseModel):
    """POST リクエスト時に受け取るデータ"""
    id: int
    keyword: str

class KeywordResponse(BaseModel):
    """レスポンスとして返すデータ"""
    id: int
    keyword: str

class Config:
    from_attributes = True  # SQLAlchemy モデルからの変換を許可