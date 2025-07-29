peliculas = []

def agregar_peliculas():
    cantidad = int(input("¿Cuántas películas desea ingresar? "))
    for _ in range(cantidad):
        titulo = input("Título: ").strip()
        año = int(input("Año de estreno: "))
        genero = input("Género: ").strip().lower()
        peliculas.append([titulo, año, genero])
    print(f"{cantidad} película(s) agregada(s) correctamente.\n")

def mostrar_peliculas():
    if not peliculas:
        print("No hay películas registradas.\n")
        return
    print("\nCatálogo de Películas:")
    for p in peliculas:
        print(f"Título: {p[0]} | Año: {p[1]} | Género: {p[2]}")
    print()

def buscar_por_genero():
    genero = input("Ingrese el género a buscar: ").strip().lower()
    encontradas = [p for p in peliculas if p[2] == genero]
    if encontradas:
        print(f"\nPelículas del género '{genero}':")
        for p in encontradas:
            print(f"- {p[0]} ({p[1]})")
    else:
        print(f"No se encontraron películas del género '{genero}'.")
    print()

def eliminar_por_titulo():
    titulo = input("Ingrese el título exacto de la película a eliminar: ").strip()
    for p in peliculas:
        if p[0].lower() == titulo.lower():
            peliculas.remove(p)
            print(f"Película '{titulo}' eliminada correctamente.\n")
            return
    print(f"No se encontró una película con el título '{titulo}'.\n")

def ver_estadisticas():
    if not peliculas:
        print("No hay películas para mostrar estadísticas.\n")
        return

    total = 0
    for _ in peliculas:
        total += 1
    print(f"\nTotal de películas: {total}")

    generos = {}
    for p in peliculas:
        genero = p[2]
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1

    print("Películas por género:")
    for genero in generos:
        print(f"- {genero}: {generos[genero]}")

    mas_antigua = peliculas[0]
    for p in peliculas[1:]:
        if p[1] < mas_antigua[1]:
            mas_antigua = p
    print(f"Película más antigua: {mas_antigua[0]} ({mas_antigua[1]})\n")

def menu():
    while True:
        print("----- MENÚ -----")
        print("1. Agregar películas")
        print("2. Mostrar todas las películas")
        print("3. Buscar películas por género")
        print("4. Eliminar una película por título")
        print("5. Ver estadísticas del catálogo")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ")

        match opcion:
            case "1":
                agregar_peliculas()
            case "2":
                mostrar_peliculas()
            case "3":
                buscar_por_genero()
            case "4":
                eliminar_por_titulo()
            case "5":
                ver_estadisticas()
            case "6":
                print("Programa finalizado.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.\n")

menu()