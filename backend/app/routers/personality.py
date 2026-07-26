from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.personality import PersonalityCreate, PersonalityResponse
from app import crud

router = APIRouter(prefix="/personalities", tags=["personalities"])

@router.get("/", response_model=list[PersonalityResponse])
def read_personalities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ユーザー一覧取得"""
    return crud.get_personalities(db, skip=skip, limit=limit)

@router.get("/{personality_id}", response_model=PersonalityResponse)
def read_personality(personality_id: int, db: Session = Depends(get_db)):
    """ユーザー1件取得"""
    personality = crud.get_personality(db, personality_id=personality_id)
    if personality_id is None:
        raise HTTPException(status_code=404, detail="Personality not found")
    return personality

@router.post("/", response_model=PersonalityResponse, status_code=201)
def create_personality(personality: PersonalityCreate, db: Session = Depends(get_db)):
    """ユーザー作成"""
    return crud.create_personality(db, personality=personality)

@router.delete("/{personality_id}", response_model=PersonalityResponse)
def delete_personality(personality_id: int, db: Session = Depends(get_db)):
    """ユーザー削除"""
    personality = crud.delete_personality(db, personality_id=personality_id)
    if personality is None:
        raise HTTPException(status_code=404, detail="Personality not found")
    return personality