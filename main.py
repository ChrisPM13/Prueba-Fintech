from fastapi import FastAPI
from app.database import Base, engine
from app.routes import applications, score, documents

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fintech Credit API", summary="API para gestión de solicitudes de crédito")

# Registrar rutas

app.include_router(applications.router, tags=["Solicitudes"])
app.include_router(score.router, tags=["Score de crédito"])
app.include_router(documents.router, tags=["Documentos"])
