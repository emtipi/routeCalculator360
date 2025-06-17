# RouteCalculator360 🚗 ✈️ ⛴️ 🚂

## Descripción General

RouteCalculator360 es una calculadora de rutas de transporte basada en Python que ayuda a los usuarios a encontrar caminos óptimos entre ciudades utilizando varios métodos de transporte. La aplicación utiliza un algoritmo de búsqueda en amplitud para determinar el camino más corto entre las ciudades de origen y destino.

## Características

- **Transporte Multimodal**: Soporta viajes en coche, avión, barco y tren
- **Interfaz Amigable**: Interfaz de línea de comandos simple para una fácil interacción
- **Búsqueda Inteligente de Rutas**: Encuentra la ruta óptima entre ciudades
- **Estructura de Datos Flexible**: Configuración de ciudades y conexiones basada en JSON

## Estructura del Proyecto

```
routeCalculator360/
├── main.py                 # Punto de entrada principal de la aplicación
├── classes/                # Directorio de clases principales
│   ├── city.py             # Definición de la clase Ciudad
│   ├── connection.py       # Definición de la clase Conexión
│   └── functions.py        # Funciones de utilidad y lógica principal
└── data/                   # Directorio de datos
    └── cities_connections.json  # Configuración de ciudades y conexiones
```

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/emtipi/routeCalculator360.git
   cd routeCalculator360
   ```

2. Asegúrate de tener Python 3.6+ instalado.

## Uso

Ejecuta la aplicación usando Python:

```bash
python main.py
```

### Usando la Aplicación:

1. Selecciona la opción 1 para calcular una ruta
2. Ingresa el nombre de la ciudad de origen
3. Ingresa el nombre de la ciudad de destino
4. Visualiza los detalles de la ruta paso a paso

## Configuración de Datos

La aplicación utiliza un archivo JSON (`data/cities_connections.json`) que contiene:

- Una lista de ciudades disponibles
- Conexiones entre ciudades con detalles de transporte

Para agregar nuevas ciudades o conexiones, edita el archivo JSON siguiendo el formato establecido.

## Detalles Técnicos

- **Procesamiento de Datos**: La aplicación normaliza los nombres de las ciudades para garantizar un procesamiento consistente independientemente del formato de entrada
- **Búsqueda de Caminos**: Implementa el algoritmo de Búsqueda en Amplitud (BFS) para encontrar el camino más corto
- **Diseño Orientado a Objetos**: Utiliza clases para ciudades y conexiones para crear un diseño modular

## Licencia

[Licencia MIT](LICENSE)

## Autor

eMTiPi 🫡