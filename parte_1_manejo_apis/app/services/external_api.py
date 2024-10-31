import httpx

from app.core.utils.constants import JSON_PLACEHOLDER_API, POKE_API

async def fetch_user(username: str):
    url = JSON_PLACEHOLDER_API
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        return next((user for user in users if user["username"] == username), None)
    
async def fetch_users():
    url = JSON_PLACEHOLDER_API
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        return users

async def fetch_pokemon(pokemon_name: str):
    url = rf"{POKE_API}/{pokemon_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
        return None
