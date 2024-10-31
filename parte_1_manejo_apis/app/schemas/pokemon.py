from pydantic import BaseModel
from typing import List

class PokemonResponse(BaseModel):
    id: int
    name: str
    types: List[str]  # Lista de tipos, cada uno con la estructura de PokemonType
    
    @classmethod
    def from_api_data(cls, data: dict) -> "PokemonResponse":
        # Realizamos la transformación de los tipos aquí
        types = [type_info["type"]["name"] for type_info in data["types"]]
        return cls(id=data["id"], name=data["name"], types=types)