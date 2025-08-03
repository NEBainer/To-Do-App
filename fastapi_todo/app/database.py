# database.py
from sqlalchemy import create_engine #Para conectar a la base de datos
from sqlalchemy.ext.declarative import declarative_base #Para definir los modelos (tablas) como clases.
from sqlalchemy.orm import sessionmaker #para crear sesiones y hacer operaciones (SELECT, INSERT, etc.).

# 1. URL de la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./usuarios.db"  #Usamos SQLite para este ejemplo, pero puedes cambiarlo a otra base de datos como PostgreSQL o MySQL. La base de datos estará en un archivo llamado usuarios.db en el mismo directorio del proyecto (./).

# 2. Crear el engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # Este parámetro es específico para SQLite. Engine es quien realmente abre la conexión a la base de datos.
)

# 3. Crear el sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base para los modelos
Base = declarative_base() #Creamos la clase base para definir nuestros modelos (tablas).

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

