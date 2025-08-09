from fastapi import FastAPI
from app.routers import usuarios, tareas
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
#Para iniciar el servidor, usa el comando: uvicorn app.main:app --reload
app.include_router(usuarios.router)
app.include_router(tareas.router)
