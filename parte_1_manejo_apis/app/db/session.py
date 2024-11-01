from sqlmodel import SQLModel, create_engine, Session

from app.core.utils.constants import DATABASE_URL

  
engine = create_engine(DATABASE_URL, echo=True)

#Inyección de la conexión de bd, para persistir las capturas.
def get_session():
    with Session(engine) as session:
        yield session

