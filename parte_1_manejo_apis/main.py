import uvicorn
from fastapi import FastAPI

#La instancia de la app de FastAPI
app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app='main:app',reload=True)