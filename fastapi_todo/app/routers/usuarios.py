# routers/usuarios.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db
from app.utils import obtener_o_404
from app.auth import get_current_user

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
)

@router.get("/me", response_model=schemas.UsuarioMostrar)
def leer_usuario_actual(usuario: models.Usuario = Depends(get_current_user)):
    return usuario

@router.get("/", response_model=List[schemas.UsuarioMostrar])
def obtener_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db, skip=skip, limit=limit)
    #return []

@router.get("/{usuario_id}", response_model=schemas.UsuarioMostrar)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return obtener_o_404(
        crud.obtener_usuario_por_id(db, usuario_id),
        "Usuario"
    )

@router.post("/", response_model=schemas.UsuarioMostrar)
def crear_usuario(usuario: schemas.UsuarioCrear, db: Session = Depends(get_db)):
    return crud.crear_usuario(db=db, usuario=usuario)

@router.put("/{usuario_id}", response_model=schemas.UsuarioMostrar)
def actualizar_usuario(usuario_id: int, usuario_actualizado: schemas.UsuarioActualizar, db: Session = Depends(get_db)):
    return obtener_o_404(
        crud.actualizar_usuario(db, usuario_id, usuario_actualizado),
        "Usuario"
    )

@router.delete("/{usuario_id}", response_model=schemas.UsuarioMostrar)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return obtener_o_404(
        crud.eliminar_usuario(db, usuario_id),
        "Usuario"
    )