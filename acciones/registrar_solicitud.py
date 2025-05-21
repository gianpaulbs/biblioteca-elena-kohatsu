import pandas as pd
from datetime import datetime, timedelta

def registrar_solicitud(lector: dict, codigo_libro: int):
    try:
        fecha_prestamo = (datetime.now() + timedelta(days=15)).strftime('%d/%m/%Y')

        nuevo_prestamo = pd.DataFrame([{
            'dni': lector['dni'],
            'nombre': lector['nombre'],
            'codigo_libro': codigo_libro,
            'fecha_prestamo': fecha_prestamo,
            'devuelto': 0
        }])

        nuevo_prestamo.to_csv("csv/prestamos.csv", mode="a", header=False, index=False)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
