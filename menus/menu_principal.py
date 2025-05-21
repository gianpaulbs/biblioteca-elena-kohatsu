from menus.menu_libros_mas_prestados import mostrar_menu_libros_mas_prestados
from menus.menu_registrar_solicitud import mostrar_menu_registrar_solicitud
from menus.menu_libros_no_devueltos import mostrar_menu_libros_no_devueltos
from utils.consola import limpiar_pantalla
from acciones.lectores import tiene_prestamo_pendiente

def menu_principal():
    limpiar_pantalla()

    while True:
        print("=== Biblioteca Elena Kohatsu ===")
        print("1. Registrar préstamo de un libro")
        print("2. Reporte de libros más prestados")
        print("3. Reporte de libros que no han sido devueltos")
        print("4. Salir")
        print("\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_registrar_solicitud()
        elif opcion == "2":
            mostrar_menu_libros_mas_prestados()
        elif opcion == "3":
            mostrar_menu_libros_no_devueltos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

        limpiar_pantalla()
