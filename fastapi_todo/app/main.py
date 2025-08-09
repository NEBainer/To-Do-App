from fastapi import FastAPI
from app.routers import usuarios, tareas
from app.database import engine, Base
from app.models import Usuario, Tarea

Base.metadata.create_all(bind=engine)
app = FastAPI()
#Ruta para moverme D:\Escritorio\Cosas\Proyectos\Portafolios\To Do App\fastapi_todo
#Para iniciar el servidor, usa el comando: uvicorn app.main:app --reload
app.include_router(usuarios.router)
app.include_router(tareas.router)
