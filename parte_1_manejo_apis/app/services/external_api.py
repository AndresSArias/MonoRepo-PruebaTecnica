from typing import List
import httpx

from app.core.utils.constants import JSON_PLACEHOLDER_API, POKE_API
from app.schemas.pokemon import PokemonResponse
from app.schemas.user import UserResponse

async def fetch_user(username: str) -> UserResponse :
    url = JSON_PLACEHOLDER_API
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        user = next((user for user in users if user["username"] == username), None)
        return UserResponse.from_api_data(user) if user is not None else user
    
async def fetch_users() -> List[UserResponse]:
    url = JSON_PLACEHOLDER_API
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        return users


async def fetch_pokemon(pokemon_name: str) -> PokemonResponse:
    url = rf"{POKE_API}/{pokemon_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            return PokemonResponse.from_api_data(data)
        
        return None