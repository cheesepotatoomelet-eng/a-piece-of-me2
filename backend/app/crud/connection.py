from sqlalchemy.orm import Session
from app.models.connection import Connections
from app.schemas.connection import ConnectionCreate

def get_connections(db: Session, skip: int = 0, limit: int = 100):
    """ユーザー一覧取得"""
    return db.query(Connection).offset(skip).limit(limit).all()

def get_connection(db: Session, connection_id: int):
    """ユーザー1件取得"""
    return db.query(Connection).filter(Connection.id == connection_id).first()

def create_connection(db: Session, connection: ConnectionCreate):
    """ユーザー作成"""
    db_connection = Connection(name=connection.name, email=connection.email)
    db.add(db_connection)
    db.commit()
    db.refresh(db_connection)
    return db_connection

def delete_connection(db: Session, connection_id: int):
    """ユーザー削除"""
    db_connection = db.query(Connection).filter(Connection.id == connection_id).first()
    if db_connection:
        db.delete(db_connection)
        db.commit()
    return db_connection