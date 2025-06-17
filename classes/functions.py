import json
import unicodedata
from classes.city import City
from classes.connection import Connection
from collections import deque

class Functions:
    def __init__(self, file_path=None):
        self.cities = []
        self.connections = []
        if file_path:
            self.load_data_json(file_path)

    def load_data_json(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)

        self.cities = [City(name) for name in data["cities"]]
        self.connections = []
        for conn in data["connections"]:
            type = conn["type"]
            origin = conn["origin"]
            destination = conn["destination"]
            kwargs = {k: v for k, v in conn.items() if k not in ["type", "origin", "destination"]}
            self.connections.append(Connection(type, origin, destination, **kwargs))

    @staticmethod
    def clean_city_name(name):
        # Eliminar acentos y caracteres especiales, dejar solo letras y espacios
        name = unicodedata.normalize('NFD', name)
        name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')
        name = ''.join(c for c in name if c.isalpha() or c.isspace())
        return name.capitalize()

    def find_route(self, origin, destination):
        # BFS para encontrar la ruta más corta
        queue = deque()
        queue.append((origin, []))
        visited = set()

        while queue:
            current_city, path = queue.popleft()
            if current_city == destination:
                return path
            visited.add(current_city)
            for conn in self.connections:
                if conn.origin == current_city and conn.destination not in visited:
                    queue.append((conn.destination, path + [conn]))
        return None

    def show_route(self, origin, destination):
        city_names = [city.name for city in self.cities]
        if origin not in city_names or destination not in city_names:
            print("Una o ambas ciudades no existen en la base de datos.")
            return
        route = self.find_route(origin, destination)
        if route is None:
            print("No existe una ruta válida entre las ciudades.")
        elif len(route) == 0:
            print("¡Ya te encuentras en tu destino!")
        else:
            for idx, conn in enumerate(route, 1):
                print(f"{idx}. {conn}")
            print("¡Felicidades, has llegado a tu destino!")
