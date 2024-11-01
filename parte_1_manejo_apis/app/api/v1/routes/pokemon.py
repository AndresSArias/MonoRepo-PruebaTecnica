from fastapi import APIRouter, HTTPException
from app.core.utils.constants import GET_POKEMON_POKEMON_NO_FOUND_404,GET_POKEMON_POKEMON_SUMMARY,GET_POKEMON_POKEMON_DESCRIPTION
from app.schemas.pokemon import PokemonResponse
from app.services.external_api import fetch_pokemon

router = APIRouter()

#Endpoint para recibir y verificar si el pokemon que se quiere capturar existe.
@router.get("/pokemon/{pokemon_name}", response_model= PokemonResponse,summary=GET_POKEMON_POKEMON_SUMMARY, description=GET_POKEMON_POKEMON_DESCRIPTION)
async def get_pokemon(pokemon_name: str):
    pokemon = await fetch_pokemon(pokemon_name)
    if not pokemon:
        raise HTTPException(status_code=404, detail=GET_POKEMON_POKEMON_NO_FOUND_404)
    return pokemon
