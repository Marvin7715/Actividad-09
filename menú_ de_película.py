peliculas = []

def agregar_peliculas():
    cantidad = int(input("¿Cuántas películas desea ingresar? "))
    for _ in range(cantidad):
        titulo = input("Título: ").strip()
        año = int(input("Año de estreno: "))
        genero = input("Género: ").strip().lower()
        peliculas.append([titulo, año, genero])
    print(f"{cantidad} película(s) agregada(s) correctamente.\n")