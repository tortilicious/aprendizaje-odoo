"""
Ejercicio A:
Dada esta lista de precios: [45, 120, 89, 200, 15, 350]

Crea una lista solo con precios mayores a 100
Crea una lista con precios + 21% IVA
Crea una lista con "Caro" si >100, "Barato" si no
"""

# Ejercicio A
precios = [45, 120, 89, 200, 15, 350]


def precios_mayores_100(precios):
    return [precio for precio in precios if precio > 100]


def precios_iva(precios):
    return [precio * 1.21 for precio in precios]


def definir_caro_barato(precios):
    return ["Caro" if precio > 100 else "Barato" for precio in precios]

