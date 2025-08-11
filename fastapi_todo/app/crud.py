# crud.py
from sqlalchemy.orm import Session
from app.models import Usuario, Tarea
from app.schemas import UsuarioCrear, UsuarioActualizar, TareaCrear, TareaActualizar
from app.auth import hash_password

# FUNCIONES CRUD PARA USUARIOS
# Crear usuario
def crear_usuario(db: Session, usuario: UsuarioCrear):
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        contraseña=hash_password(usuario.contraseña)
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

# Obtener usuario por email
def obtener_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

# Actualizar usuario
def actualizar_usuario(db: Session, usuario_id: int, usuario_actualizado: UsuarioActualizar):
    db_usuario = obtener_usuario_por_id(db, usuario_id)
    if db_usuario is None:
        return None
    for key, value in usuario_actualizado.model_dump(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Eliminar usuario
def eliminar_usuario(db: Session, usuario_id: int):
    usuario = obtener_usuario_por_id(db, usuario_id)
    if usuario is None:
        return None
    db.delete(usuario)
    db.commit()
    return usuario

# FUNCIONES CRUD PARA TAREAS
def crear_tarea(db: Session, tarea: TareaCrear, usuario_id: int):
    nueva_tarea = Tarea(**tarea.model_dump(), usuario_id=usuario_id)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def obtener_tareas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tarea).offset(skip).limit(limit).all()

def obtener_tarea_por_id(db: Session, tarea_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea_actualizada: TareaActualizar):
    db_tarea = obtener_tarea_por_id(db, tarea_id)
    if not db_tarea:
        return None
    for key, value in tarea_actualizada.model_dump(exclude_unset=True).items():
        setattr(db_tarea, key, value)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def eliminar_tarea(db: Session, tarea_id: int):
    db_tarea = obtener_tarea_por_id(db, tarea_id)
    if not db_tarea:
        return None
    db.delete(db_tarea)
    db.commit()
    return db_tarea
