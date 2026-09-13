from pydantic import BaseModel, EmailStr
from datetime import datetime

class KeywordCreate(BaseModel):
    """POST リクエスト時に受け取るデータ"""
    id: int
    keywords: str

class KeywordResponse(BaseModel):
    """レスポンスとして返すデータ"""
    id: int
    keywords: str

class Config:
    from_attributes = True  # SQLAlchemy モデルからの変換を許可