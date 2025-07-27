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