"""
Ejercicio C:
Con tus ventas: [120, 340, 89, 230, 410, 95, 180, 265, 150, 320]

Usa enumerate para crear lista: ["Día 1: 120€", "Día 2: 340€", ...]
Crea lista con índices de días donde venta < 100
Crea diccionario: {1: 120, 2: 340, ...}
"""

# Ejercicio C
ventas = [120, 340, 89, 230, 410, 95, 180, 265, 150, 320]
def lista_dias_ventas(ventas):
    return [f"Dia: {dia}: {venta}$"for (dia, venta) in enumerate(ventas, start=1)]

# Crea lista con índices de días donde venta < 100
def dias_venta_inferior_100(ventas):
    return [dia for (dia, venta) in enumerate(ventas, start=1) if venta < 100]

# Crea diccionario: {1: 120, 2: 340, ...}
def diccionario_dias_ventas(ventas):
    return {dia: venta for (dia, venta) in enumerate(ventas, start=1)}