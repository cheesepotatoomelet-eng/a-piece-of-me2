from sqlalchemy.orm import Session
from app.models.user_keywords import User_keyword

def get_user_keyword(db: Session, user_id: int):
    """ユーザー1件取得"""
    return db.query(User_keyword).filter(User_keyword.user_id == user_id)
