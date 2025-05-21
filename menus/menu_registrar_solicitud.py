from utils.consola import limpiar_pantalla
from menus.menu_seleccionar_libros import mostrar_menu_seleccionar_libro
from acciones.lectores import obtener_lector_por_dni, registrar_lector, tiene_prestamo_pendiente
from acciones.registrar_solicitud import registrar_solicitud

def mostrar_menu_registrar_solicitud():
    limpiar_pantalla()

    print("Registrar solicitud de préstamo")

    dni = input("\nIngrese DNI del lector: ")

    lector = obtener_lector_por_dni(dni)

    if not lector:
        nombre = input("Ingrese nombre y apellidos: ")
        lector = registrar_lector(dni, nombre)

    if tiene_prestamo_pendiente(dni):
        input("\nPresione cualquier tecla para volver...")
        return
    
    libro_seleccionado = mostrar_menu_seleccionar_libro()

    registro_exitoso = registrar_solicitud(lector, libro_seleccionado)

    if (registro_exitoso):
        print("El registro de la solicitud se realizó satisfactoriamente")
    else:
        print("Hubo un error al momento de registrar la solicitud de préstamo.")

    input("\nPresione cualquier tecla para volver...")