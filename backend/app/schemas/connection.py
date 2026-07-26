from pydantic import BaseModel, EmailStr
from datetime import datetime

class ConnectionCreate(BaseModel):
    """POST リクエスト時に受け取るデータ"""
    id: int
    connection: str

class ConnectionResponse(BaseModel):
    """レスポンスとして返すデータ"""
    id: int
    connection: str

class Config:
    from_attributes = True  # SQLAlchemy モデルからの変換を許可