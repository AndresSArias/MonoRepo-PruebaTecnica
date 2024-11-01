from pydantic import BaseModel

#Mediante Pydantic, creamos el modelo que recibiremos desde la API Externa.
class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str

    #Mappeador de json a instancia de este modelo
    @classmethod
    def from_api_data(cls, data: dict) -> "UserResponse":

        return cls(id=data["id"], name=data["name"], username=data["username"],email=data["email"])