import pandas as pd

def obtener_lector_por_dni(dni: str):
    try:
        df = pd.read_csv("csv/lectores.csv", dtype={"dni": str})
        fila = df[df["dni"] == dni]

        if fila.empty:
            return None
        
        return fila.iloc[0].to_dict()
    except FileNotFoundError:
        return None

def registrar_lector(dni: str, nombre: str):
    df = pd.DataFrame([[dni, nombre]], columns=["dni", "nombre"])
    df.to_csv("csv/lectores.csv", mode="a", header=False, index=False)

    return { "dni": dni, "nombre": nombre }

def tiene_prestamo_pendiente(dni:str) -> bool:
    try:
        df = pd.read_csv("csv/prestamos.csv")
        prestamos_pendientes = df[
            (df["dni"].astype(str) == dni) & 
            (df["devuelto"] == 0)
        ]
        
        if not prestamos_pendientes.empty:
            print(f"El lector con DNI {dni} tiene {len(prestamos_pendientes)} préstamo(s) pendiente(s).")
            return True
        else:
            return False
    except FileNotFoundError:
        print("El archivo de préstamos no fue encontrado.")
        return False
