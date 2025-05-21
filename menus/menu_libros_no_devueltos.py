from utils.consola import limpiar_pantalla
from acciones.reportes import obtener_libros_sin_devolver

def mostrar_menu_libros_no_devueltos():
    limpiar_pantalla()

    print("Libros que no han sido devueltos:\n")
    resultado = obtener_libros_sin_devolver()

    if not resultado:
        print("No hay libros sin devolver.")
    else:
        print("{:<45}".format("Título"))
        print("-" * 45)
        
        for fila in resultado:
            print("{:<45}".format(fila[0]))

    input("\nPresione cualquier tecla para volver...")