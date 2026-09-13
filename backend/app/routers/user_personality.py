from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_personality import User_personalityResponse, User_personalityCreate
from app import crud

router = APIRouter(prefix="/user_personalities", tags=["user_personalities"])

@router.get("/{user_personality_id}", response_model=User_personalityResponse)
def read_user_personality_id(user_personality_id: int, db: Session = Depends(get_db)):
    """ユーザー1件取得"""
    personality = crud.get_user_personality(db, user_personality_id=user_personality_id)
    if user_personality_id is None:
        raise HTTPException(status_code=404, detail="personality not found")
    return personality

@router.post("/", response_model=User_personalityResponse, status_code=201)
def create_user_personality(user_personality: User_personalityCreate, db: Session = Depends(get_db)):
    """ユーザー作成"""
    return crud.create_user_personality(db, user_personality=user_personality)
