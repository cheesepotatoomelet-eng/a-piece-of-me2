from sqlalchemy.orm import Session
from app.models.keyword import Keywords
from app.schemas.keyword import KeywordCreate

def get_keywords(db: Session, skip: int = 0, limit: int = 100):
    """ユーザー一覧取得"""
    return db.query(Keywords).offset(skip).limit(limit).all()

def get_keyword(db: Session, keyword_id: int):
    """ユーザー1件取得"""
    return db.query(Keywords).filter(Keywords.id == keyword_id).first()

def create_keyword(db: Session, keyword: KeywordCreate):
    """ユーザー作成"""
    db_keyword = Keywords(name=keyword.name, email=keyword.email)
    db.add(db_keyword)
    db.commit()
    db.refresh(db_keyword)
    return db_keyword

def delete_keyword(db: Session, keyword_id: int):
    """ユーザー削除"""
    db_keyword = db.query(Keywords).filter(Keywords.id == keyword_id).first()
    if db_keyword:
        db.delete(db_keyword)
        db.commit()
    return db_keyword