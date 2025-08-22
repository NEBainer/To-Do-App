from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from app.database import Base  

class Usuario(Base):
    __tablename__ = "usuarios"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True) 
    nombre = Column(String, index=True)  
    email = Column(String, unique=True, index=True) 
    contraseña = Column(String)  
    tareas = relationship("Tarea", back_populates="usuario")
    
class Tarea(Base):
    __tablename__ = "tareas" 

    id = Column(Integer, primary_key = True, index = True)
    titulo = Column(String, index = True)
    descripcion = Column(String, nullable= True)
    completada = Column(Boolean, default= False)
    fecha_creacion = Column(DateTime, default = datetime.astimezone(datetime.now()))
    usuario_id = Column(Integer, ForeignKey("usuarios.id")) 

    usuario = relationship("Usuario", back_populates="tareas") 