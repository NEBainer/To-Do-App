# crud.py

from sqlalchemy.orm import Session
from app.models import Usuario
from app.schemas import UsuarioCrear

# Crear usuario
def crear_usuario(db: Session, usuario: UsuarioCrear):
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        contraseña=usuario.contraseña
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Obtener todos los usuarios
def obtener_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

# Obtener un usuario por ID
def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()
