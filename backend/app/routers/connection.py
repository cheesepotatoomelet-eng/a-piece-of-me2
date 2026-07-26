from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.connection import ConnectionCreate, ConnectionResponse
from app import crud

router = APIRouter(prefix="/connections", tags=["connections"])

@router.get("/", response_model=list[ConnectionResponse])
def read_connections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ユーザー一覧取得"""
    return crud.get_connections(db, skip=skip, limit=limit)

@router.get("/{connection_id}", response_model=ConnectionResponse)
def read_connection(connection_id: int, db: Session = Depends(get_db)):
    """ユーザー1件取得"""
    connection = crud.get_connection(db, connection_id=connection_id)
    if connection is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return connection

@router.post("/", response_model=ConnectionResponse, status_code=201)
def create_connection(connection: ConnectionCreate, db: Session = Depends(get_db)):
    """ユーザー作成"""
    return crud.create_connection(db, connection=connection)

@router.delete("/{connection_id}", response_model=ConnectionResponse)
def delete_connection(connection_id: int, db: Session = Depends(get_db)):
    """ユーザー削除"""
    connection = crud.delete_connection(db, connection_id=connection_id)
    if connection is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return connection