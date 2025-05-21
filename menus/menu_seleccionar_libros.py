from acciones.libros import obtener_libros

def mostrar_menu_seleccionar_libro() -> int:
    df = obtener_libros()

    if df.empty:
        print("No hay libros disponibles.")
        return -1

    print("\nLibros disponibles:")
    for i, row in df.iterrows():
        print(f"{i + 1}. {row['titulo']}")

    while True:
        opcion = input("\nSeleccione el número del libro: ")

        if opcion.isdigit() and 1 <= int(opcion) <= len(df):
            index = int(opcion) - 1
            return int(df.iloc[index]["codigo"])
        else:
            print("Opción inválida. Intente de nuevo.")
