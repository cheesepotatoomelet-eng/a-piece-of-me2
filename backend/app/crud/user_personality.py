from sqlalchemy.orm import Session
from app.models.user_personalities import User_personality
from app.schemas.user_personality import User_personalityCreate

def get_user_personality(db: Session, user_id: int):
    """ユーザー1件取得"""
    return db.query(User_personality).filter(User_personality.user_id == user_id)

def create_user_personality(db: Session, user_personality: User_personalityCreate):
    """ユーザー作成"""
    for personality in user_personality.personality_id:
        db_user_personality = User_personality(user_id=user_personality.user_id, personality_id=personality)
        db.add(db_user_personality)
        db.commit()
        db.refresh(db_user_personality)
    return db_user_personality