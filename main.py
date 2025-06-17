from classes.functions import Functions

def main():
    print("=" * 58)
    print("🚗 ✈️  Bienvenido al Calculador de Rutas Calibre360 ⛴️  🚂")
    print("=" * 58)

    # Instanciar la clase y cargar los datos
    f = Functions('data/cities_connections.json')

    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Calcular ruta")
        print("2. Salir")
        option = input("Selecciona una opción (1/2): ").strip()

        if option == "1":
            origin = input("Ciudad de origen: ").strip()
            destination = input("Ciudad de destino: ").strip()
            # Limpiar los nombres introducidos
            originClean = f.clean_city_name(origin)
            destinationClean = f.clean_city_name(destination)
            print(f"\nCalculando ruta de {originClean} a {destinationClean}...\n")
            f.show_route(originClean, destinationClean)
        elif option == "2":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

if __name__ == "__main__":
    main()