# Solución ejercicio 10

def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                yield linea.strip()
    except FileNotFoundError:
        print(f"Archivo {ruta_archivo} no encontrado")

for linea in leer_archivo("/media/miguel/programacion/Python/aprendizaje-odoo/dia_6/teoria/Guia_generadores.md"):
    print(linea)
