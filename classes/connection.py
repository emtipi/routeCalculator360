class Connection:
    def __init__(self, type, origin, destination, **kwargs):
        self.type = type
        self.origin = origin
        self.destination = destination
        self.attributes = kwargs

    def __str__(self):
        if self.type == 'Train':
            return f"Coge el tren {self.attributes.get('flight_number', '')} con asiento {self.attributes.get('seat', '')} desde {self.origin} hasta {self.destination}."
        elif self.type == 'Plane':
            return f"Coge el avión {self.attributes.get('flight_number', '')} con asiento {self.attributes.get('seat', '')} desde {self.origin} hasta {self.destination}."
        elif self.type == 'Car':
            return f"Coge el coche con matrícula {self.attributes.get('plate', '')} desde {self.origin} hasta {self.destination}."
        elif self.type == 'Ship':
            return f"Coge el barco {self.attributes.get('ship_number', '')} desde {self.origin} hasta {self.destination}."
        else:
            return "⚠️Tipo de vehículo desconocido⚠️"
