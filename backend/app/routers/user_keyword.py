from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_keyword import UserKeywordResponse
from app import crud

router = APIRouter(prefix="/user_keywords", tags=["user_keywords"])

@router.get("/{user_keyword_id}", response_model=UserKeywordResponse)
def read_keyword_id(keyword_id: int, db: Session = Depends(get_db)):
    """ユーザー1件取得"""
    keyword = crud.get_user_keyword(db, keyword_id=keyword_id)
    if keyword_id is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return keyword