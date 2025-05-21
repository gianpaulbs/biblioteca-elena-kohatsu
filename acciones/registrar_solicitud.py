import pandas as pd
from datetime import datetime, timedelta

def registrar_solicitud(dni, codigo_libro):
    try:
        lectores = pd.read_csv("csv/lectores.csv")
        libros = pd.read_csv("csv/libros.csv")
        prestamos = pd.read_csv("csv/prestamos.csv")

        # Verificar si el lector está registrado
        if dni not in lectores['dni'].astype(str).values:
            return "Lector no registrado en el sistema."

        # Verificar si el libro existe y está disponible
        libro = libros[libros['codigo'] == codigo_libro]
        if libro.empty:
            return "El código del libro no existe."
        
        if libro.iloc[0]['estado'] != 'disponible':
            return "El libro no está disponible para préstamo."

        # Registrar préstamo
        fecha_prestamo = datetime.now().strftime('%Y-%m-%d')
        fecha_devolucion = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

        nuevo_prestamo = {
            'dni': dni,
            'codigo_libro': codigo_libro,
            'fecha_prestamo': fecha_prestamo,
            'fecha_devolucion': fecha_devolucion,
            'estado': 'prestado'
        }

        prestamos = pd.concat([prestamos, pd.DataFrame([nuevo_prestamo])], ignore_index=True)
        prestamos.to_csv("csv/prestamos.csv", index=False)

        # Actualizar estado del libro
        libros.loc[libros['codigo'] == codigo_libro, 'estado'] = 'prestado'
        libros.to_csv("csv/libros.csv", index=False)

        return f"Solicitud registrada. Fecha de devolución: {fecha_devolucion}"

    except FileNotFoundError:
        return "Uno o más archivos CSV no fueron encontrados."
    except Exception as e:
        return f"Error: {e}"
