#Constantes con las url a las API y conexión de bd.
JSON_PLACEHOLDER_API = r'https://jsonplaceholder.typicode.com/users'
POKE_API = r'https://pokeapi.co/api/v2/pokemon'
DATABASE_URL = "sqlite:///./app/db/capturas.db"

#Constantes documentación
GET_USERS_USERS_SUMMARY = "Obtener personas."
GET_USERS_USERS_DESCRIPTION = "Mira y verifica las personas con sus atributos, que pueden capturar un pokémon."
GET_POKEMON_POKEMON_SUMMARY = "Obtener pokemon."
GET_POKEMON_POKEMON_DESCRIPTION = "Mira y verifica la existencia de un pokémon por su id en la Pokédex o el nombre del pokemon."
CAPTURE_POKEMON_SUMMARY = "Hacer captura de Pokémon."
CAPTURE_POKEMON_DESCRIPTION = "Crea una nueva captura de un pokémon existente por una persona validada."
GET_CAPTURES_SUMMARY = "Mostrar capturas."
GET_CAPTURES_DESCRIPTION = "Mira las capturas realizadas por parte de las personas hacia los pokémones"
#Constantes para el manejo de errores
CAPTURE_POKEMON_USER_NO_FOUND_404 = "La persona con ese usuario no exite verifique con el endpoint correspondiente."
CAPTURE_POKEMON_POKEMON_NO_FOUND_404 = "El pokémon no existe verifique con el endpoint correspondiente."
GET_POKEMON_POKEMON_NO_FOUND_404 = "El pokémon no existe, verifique el id de la pokédex ingresado o el nombre del pokemon."
GET_USERS_USERS_NO_FOUND_404 = "No hay usuarios registrados en la api."
GET_CAPTURES_CAPTURES_NO_FOUND_404 = "No se ha hecho ninguna captura."