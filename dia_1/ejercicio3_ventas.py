# Ejercicio 3. Bucles - Control de ventas

ventas_diarias = [120, 340, 89, 230, 410, 95, 180, 265, 150, 320]


# Cálculo total ventas diarias
def calcular_ventas_totales_diarias(ventas):
    return sum(ventas)


# Día con mayor número de ventas
def maximas_ventas_diarias(ventas):
    return max(ventas)


def dia_maximas_ventas(ventas):
    max_venta = max(ventas)
    return ventas.index(max_venta) + 1


# Cuantos días superaron los 200$
def dias_superado_objetivo_ventas(ventas, objetivo=200):
    return sum(1 for venta in ventas if venta > objetivo)


def promedio_ventas_diarias(ventas):
    return calcular_ventas_totales_diarias(ventas) / len(ventas)
