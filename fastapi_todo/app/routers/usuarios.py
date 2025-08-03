# routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
)

@router.get("/", response_model=List[schemas.UsuarioMostrar])
def obtener_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db, skip=skip, limit=limit)
    #return []

@router.get("/{usuario_id}", response_model=schemas.UsuarioMostrar)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_usuario_por_id(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.post("/", response_model=schemas.UsuarioMostrar)
def crear_usuario(usuario: schemas.UsuarioCrear, db: Session = Depends(get_db)):
    return crud.crear_usuario(db=db, usuario=usuario)
