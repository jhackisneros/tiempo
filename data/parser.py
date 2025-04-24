import csv

def get_week_data(nombre_semana):
    datos = []
    with open("data/records.csv", newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["semana"] == nombre_semana:
                datos.append((fila["hora"], fila["clima"]))
    return datos
