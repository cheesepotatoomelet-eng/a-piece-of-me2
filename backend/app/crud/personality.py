from sqlalchemy.orm import Session
from app.models.personality import Personality
from app.schemas.personality import PersonalityCreate

def get_personalities(db: Session, skip: int = 0, limit: int = 100):
    """ユーザー一覧取得"""
    return db.query(Personality).offset(skip).limit(limit).all()

def get_personalitie(db: Session, personalities_id: int):
    """ユーザー1件取得"""
    return db.query(Personality).filter(Personality.id == personalities_id).first()

def create_personalitie(db: Session, personality: PersonalityCreate):
    """ユーザー作成"""
    db_personality = Personality(name=personality.name, email=personality.email)
    db.add(db_personality)
    db.commit()
    db.refresh(db_personality)
    return db_personality

def delete_personalitie(db: Session, personalitie_id: int):
    """ユーザー削除"""
    db_personality = db.query(Personality).filter(Personality.id == personalitie_id).first()
    if db_personality:
        db.delete(db_personality)
        db.commit()
    return db_personality