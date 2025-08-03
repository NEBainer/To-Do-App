from pydantic import BaseModel

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
