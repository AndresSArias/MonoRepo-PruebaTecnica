
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.v1.routes import user, pokemon, capture
from app.db.session import engine  
from app.db import base  

# Define la función lifespan para gestionar el ciclo de vida de la app
@asynccontextmanager
async def lifespan(app: FastAPI):

    # Ejecuta al inicio
    base.SQLModel.metadata.create_all(bind=engine)
    yield 

#Función inicializadora de la instancia del proyecto FastAPI()
def create_app():
    
    # Crear la aplicación FastAPI con el parámetro lifespan
    app = FastAPI(lifespan=lifespan)

    # Incluir rutas
    app.include_router(user.router, prefix="/api/v1")
    app.include_router(pokemon.router, prefix="/api/v1")
    app.include_router(capture.router, prefix="/api/v1")

    #Redirección de la ruta Inicial a la documentación
    @app.get("/", include_in_schema=False, response_class=RedirectResponse)
    async def redirect_to_swagger():    
        return RedirectResponse(url="/docs")    

    return app