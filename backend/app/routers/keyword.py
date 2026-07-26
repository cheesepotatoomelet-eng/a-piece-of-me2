from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.keyword import KeywordCreate, KeywordResponse
from app import crud

router = APIRouter(prefix="/keywords", tags=["keywords"])

@router.get("/", response_model=list[KeywordResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ユーザー一覧取得"""
    return crud.get_keywords(db, skip=skip, limit=limit)

@router.get("/{keyword_id}", response_model=KeywordResponse)
def read_keyword(keyword_id: int, db: Session = Depends(get_db)):
    """ユーザー1件取得"""
    user = crud.get_keyword(db, keyword_id=keyword_id)
    if keyword_id is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return keyword

@router.post("/", response_model=KeywordResponse, status_code=201)
def create_keyword(user: KeywordCreate, db: Session = Depends(get_db)):
    """ユーザー作成"""
    return crud.create_keyword(db, keyword=keyword)

@router.delete("/{keyword_id}", response_model=KeywordResponse)
def delete_keyword(keyword_id: int, db: Session = Depends(get_db)):
    """ユーザー削除"""
    keyword = crud.delete_keyword(db, keyword_id=keyword_id)
    if keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return keyword