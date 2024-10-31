
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.routes import user, pokemon, capture
from app.db.session import engine  # Importa el engine desde session.py
from app.db import base  # Importa base para asegurar que los modelos están listos

# Define la función lifespan para gestionar el ciclo de vida de la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ejecuta al inicio
    base.SQLModel.metadata.create_all(bind=engine)
    yield  # Aquí es cuando la app comienza a recibir solicitudes
    # Código de cierre (se ejecuta al detener la app, si es necesario)


def create_app():
    
    # Crear la aplicación FastAPI con el parámetro lifespan
    app = FastAPI(lifespan=lifespan)

    # Incluir rutas
    app.include_router(user.router, prefix="/api/v1")
    app.include_router(pokemon.router, prefix="/api/v1")
    app.include_router(capture.router, prefix="/api/v1")

    return app