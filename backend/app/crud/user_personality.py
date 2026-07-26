from sqlalchemy.orm import Session
from app.models.user_personalities import User_personality

def get_user_personality(db: Session, user_id: int):
    """ユーザー1件取得"""
    return db.query(User_personality).filter(User_personality.user_id == user_id)
