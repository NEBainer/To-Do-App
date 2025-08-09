from pydantic import BaseModel
from datetime import datetime


# ===== USUARIOS =====
# Esquema para mostrar un usuario
class UsuarioBase(BaseModel):
    nombre: str
    email: str

# Esquema para crear un usuario (requiere contraseña)
class UsuarioCrear(UsuarioBase):
    contraseña: str

# Esquema para devolver un usuario (con ID)
class UsuarioMostrar(UsuarioBase):
    id: int

    class Config:
        orm_mode = True  # Necesario para que funcione con modelos ORM (SQLAlchemy)

#Esquema para actualizar un usuario (opcional)
class UsuarioActualizar(BaseModel):
    nombre: str | None = None
    email: str | None = None
    contraseña: str | None = None

# ===== TAREAS =====
class TareaBase(BaseModel):
    titulo: str
    descripcion: str | None
    completada: bool = False

class TareaCrear(TareaBase):
    pass

class TareaActualizar(BaseModel):
    titulo: str | None
    descripcion: str | None
    completada: bool | None

class TareaMostrar(TareaBase):
    id: int
    fecha_creacion: datetime
    usuario_id: int

    class Config:
        orm_mode = True