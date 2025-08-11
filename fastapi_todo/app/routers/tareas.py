from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db
from app.utils import obtener_o_404
from app.auth import get_current_user

router = APIRouter(
    prefix = "/tareas",
    tags= ["tareas"],
)

@router.get("/me", response_model=schemas.UsuarioMostrar)
def leer_usuario_actual(usuario: models.Usuario = Depends(get_current_user)):
    return usuario

@router.get("/", response_model = List[schemas.TareaMostrar])
def obtener_tareas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.obtener_tareas(db, skip = skip, limit = limit)

@router.get("/{tarea_id}", response_model = schemas.TareaMostrar)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    return obtener_o_404(
        crud.obtener_tarea_por_id(db, tarea_id),
        "Tarea"
    )

@router.post("/", response_model= schemas.TareaMostrar)
def crear_tarea(tarea: schemas.TareaCrear, db: Session = Depends(get_db)):
    return crud.crear_tarea(db = db, tarea = tarea)

@router.put("/{tarea_id}", response_model= schemas.TareaMostrar)
def actualizar_tarea(tarea_id: int, tarea_actualizada: schemas.TareaActualizar, db: Session = Depends(get_db)):
    return obtener_o_404(
        crud.actualizar_tarea(db, tarea_id, tarea_actualizada),
        "Tarea"
    )

@router.delete("/{tarea_id}", response_model= schemas.TareaMostrar)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    return obtener_o_404(
        crud.eliminar_tarea(db, tarea_id),
        "Tarea"
    )