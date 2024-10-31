JSON_PLACEHOLDER_API = r'https://jsonplaceholder.typicode.com/users'
POKE_API = r'https://pokeapi.co/api/v2/pokemon'

DATABASE_URL = "sqlite:///./app/db/capturas.db"


#Constantes para el manejo de errores
CAPTURE_POKEMON_USER_NO_FOUND_404 = "La persona con ese usuario no exite verifique con el endpoint correspondiente."
CAPTURE_POKEMON_POKEMON_NO_FOUND_404 = "El pokémon no existe verifique con el endpoint correspondiente."
GET_POKEMON_POKEMON_NO_FOUND_404 = "El pokémon no existe, verifique el id de la pokédex ingresado o el nombre del pokemon."
GET_USERS_USERS_NO_FOUND_404 = "No hay usuarios registrados en la api."
GET_CAPTURES_CAPTURES_NO_FOUND_404 = "No se ha hecho ninguna captura."