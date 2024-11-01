from app import create_app
import uvicorn

#Uso de la función create_app, para inicializar FastAPI, desde el __init__ del proyecto.
app = create_app()

if __name__ == '__main__':
    uvicorn.run(app='main:app',reload=True) 