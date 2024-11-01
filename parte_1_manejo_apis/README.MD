# CAPTURA TU POKÉMON
En este proyecto de Python con FastApi, creamos un API capaz de mediante los usuarios de la API [{JSON}Placeholder](https://jsonplaceholder.typicode.com/) y los pokémones de [PokéApi](https://pokeapi.co/). ¡Lograr una captura!

## APIS USADAS
[{JSON}Placeholder](https://jsonplaceholder.typicode.com/). Es un API libre, con información falsa y fiable para pruebas, donde tomaremos su sección de usuarios. ¡Personas que desean capturar pokémones!
Se hace un get de todos los usuarios para mostrar la información traida desde https://jsonplaceholder.typicode.com/users
![{JSON}Placeholder](static\JsonPlaceHolder.png)
[PokéApi](https://pokeapi.co/). Es una API con todos los datos de Pokémon que se pueda necesitar, en nuestro caso accederemos a la información de los pokémones, así https://pokeapi.co/api/v2/pokemon/{id}. Donde id es el número en la pokédex.
![PokéApi](static/\PokeApi.png)

## INSTALACIÓN
Ya dentro de esta carpeta en una consola realizamos lo siguiente:
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt

## EJECUCIÓN
Inmediatamente después de la instalación previa, colocamos.
1. python main.py

Así lograremos ejecutar el software, por favor siga este link para interactuar con el mismo. http://localhost:8000/

Si en la consola no está activo el entorno de desarrollo, no sale lo siguiente en la consola:
![venv_activo](static\venv_activo.png)
Ejecutamo:
1. venv\Scripts\activate
2. python main.py

y así lograriamos desplegar nuestra API.

## EJEMPLOS
### Endpoint de Obtener personas.
![obtener_personas](static\getUser.png)
Es un endpoint que responde a un método get, que no tiene entrada de datos,y su salida es una lista de posibles Personas para capturar un pokémon.
El endpoint se consume desde, http://127.0.0.1:8000/api/v1/users/

### Endpoint de Obtener pokemon.
![obtener_pokemon](static\getUser.png)
Es un endpoint que responde a un método get, que tiene de entrada una path variable, pokemon_name, el cual es String que representa un valor número de la Pokédex o el mismo nombre del pokémon que se desea obtener, funciona para validar si un pokémon existe.
El endpoint se consume desde, http://localhost:8000/api/v1/pokemon/{pokemon_name}

### Endpoint de Hacer captura de pokémon.
![capturarPokemon](static\capturePokemon.png)
Es un endpoint que responde a un método put, que tiene de entrada dos path variables, username y pokemon_name, el cuales son String, username es un nombre de identificación que suele ser fácil de recordar para las personas, este se logra captar del Endpoint Obtener persona por otro lado el pokemon_name, es un valor número de la Pokédex o el mismo nombre del pokémon a capturar, se validad la existencia de las 2 anteriores entidades y se genera un registro en una persistencia sqlite de las captura hecha.

### Endpoint de Mostrar Capturas
![mostrarCapturas](static\mostrarCapturas.png)
Es un endpoint que responde a un método get, que no tiene entrada de datos,y su salida es una lista de capturas realizadas con la API.
## ORGANIZACIÓN DEL PROYECTO
El proyecto se le implementa un tipo de arquitectura limpia, donde se puede modular los endpoints de la API y separaciones de funcionalidades por archivo.
```
    app/
    ├── api/
    │   └── v1/
    │       ├── routes/
    │       │   ├── capture.py              # Endpoint para manejar capturas
    │       │   ├── pokemon.py              # Endpoint para manejar Pokémon
    │       │   ├── user.py                 # Endpoint para manejar usuarios
    │       │   └── __init__.py
    │       └── __init__.py
    │
    ├── core/
    │   ├── utils/
    │   │   ├── constants.py                # Constantes y configuraciones
    │   │   └── __init__.py
    │   └── __init__.py
    │
    ├── db/
    │   ├── base.py                         # Base para los modelos
    │   ├── session.py                      # Configuración de la sesión de BD
    │   └── __init__.py
    │
    ├── models/
    │   ├── capture.py                      # Modelo de captura
    │   └── __init__.py
    │
    ├── schemas/
    │   ├── pokemon.py                      # Esquema para Pokémon
    │   ├── user.py                         # Esquema para usuarios
    │   └── __init__.py
    │
    ├── services/
    │   ├── external_api.py                 # Servicios de llamadas a APIs externas
    │   └── __init__.py
    │
    └── __init__.py
    │
    main.py                                 # Punto de entrada de la aplicación FastAPI


```