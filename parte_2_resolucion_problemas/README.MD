# MANEJA TUS LEADS
En este proyecto de Python busca cargar cualquier archivo .csv con la información de tus leads para manipularlos y realizar filtros que te puedan ayudar en la toma de decisiones, análisis de datos.

## INSTALACIÓN
Ya dentro de esta carpeta en una consola realizamos lo siguiente:
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt

## EJECUCIÓN
Inmediatamente después de la instalación previa, colocamos.
1. python main.py

Así lograremos ejecutar el software, por favor siga con el menú en consola.

Si en la consola no está activo el entorno de desarrollo, no sale lo siguiente en la consola:

![venv_activo](static\venv_activo.png)

Ejecutamo:
1. venv\Scripts\activate
2. python main.py

y así lograriamos desplegar nuestra el proyecto en consola.
## EJEMPLOS
### Filtrar por ubicación

![Filtrado_Ubicación](static\filto_ubi.png)

Es la primera opción que debemos seleccionar, está soportada para aceptar sólo opciones validas.

### Calcular Total

![calculo_total](static\calcular_total.png)

Es la ejecución de la función que calcula el presupuesto total de los leads filtrados por ubicación anteriormente.

### Ordenar Leads

![order_leads](static\order_leads.png)

Es la ejecución de la función que ordena los leads filtrados por ubicación anteriormente.

## ORGANIZACIÓN DEL PROYECTO
El proyecto se le implementó una arquitectura Modelo, Vista y Controlador, donde se puede separar la presentación de la aplicación que en este caso fue mediante consola, el modelo que contiene las lógicas del negocio como fue la carga del archivo y sus filtrados con pandas para mayor eficiencia y por último el controlador donde se articula la vista y el modelo.

```
    data/
    ├── leads.csv                          # Archivo CSV de datos de leads

    src/
    ├── utils/
    │   └── constants.py                   # Archivo para definir constantes
    │
    ├── controlador.py                     
    ├── modelo.py                           
    ├── vista.py                           
    └── __init__.py

    main.py                                # Punto de entrada de la aplicación

```