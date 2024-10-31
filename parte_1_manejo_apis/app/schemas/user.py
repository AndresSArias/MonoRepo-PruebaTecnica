# app/schemas/user.py
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str

    @classmethod
    def from_api_data(cls, data: dict) -> "UserResponse":

        return cls(id=data["id"], name=data["name"], username=data["username"],email=data["email"])