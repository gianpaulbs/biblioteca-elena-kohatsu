import pandas as pd

def obtener_libros():
    try:
        df = pd.read_csv("csv/libros.csv")
        return df
    except FileNotFoundError:
        print("No se encontró el archivo libros.csv.")
        return pd.DataFrame()