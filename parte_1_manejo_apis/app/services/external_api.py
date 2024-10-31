import httpx

async def fetch_user(username: str):
    url = "https://jsonplaceholder.typicode.com/users"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        return next((user for user in users if user["username"] == username), None)
    
async def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        users = response.json()
        return users

async def fetch_pokemon(pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
        return None
