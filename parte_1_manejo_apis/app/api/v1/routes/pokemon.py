from fastapi import APIRouter, HTTPException
from app.core.utils.constants import GET_POKEMON_POKEMON_NO_FOUND_404
from app.services.external_api import fetch_pokemon

router = APIRouter()

@router.get("/pokemon/{pokemon_name}")
async def get_pokemon(pokemon_name: str):
    pokemon = await fetch_pokemon(pokemon_name)
    if not pokemon:
        raise HTTPException(status_code=404, detail=GET_POKEMON_POKEMON_NO_FOUND_404)
    return pokemon
