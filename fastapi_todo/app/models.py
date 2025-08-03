from sqlalchemy import Column, Integer, String
from app.database import Base  # Importamos la base declarativa que creamos en database.py

class Usuario(Base):
    __tablename__ = "usuarios"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # ID autoincremental
    nombre = Column(String, index=True)  # Nombre del usuario
    email = Column(String, unique=True, index=True)  # Email único por usuario
    contraseña = Column(String)  # Contraseña (¡luego veremos cómo hashearla!)
