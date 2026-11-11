import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_csv(nombre_archivo):
    """Lee un CSV de la carpeta data/ y devuelve una lista de diccionarios."""
    with open(DATA_DIR / nombre_archivo, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))
