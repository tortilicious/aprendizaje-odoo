"""
Sistema de Análisis de Ventas Completo

Crea un programa que:
1. Tenga ventas de 3 productos diferentes (listas separadas)
2. Calcule estadísticas por producto (total, promedio, máximo)
3. Identifique qué producto tuvo el mejor día
4. Genere un reporte consolidado con formato

Usa:
- Funciones
- Comprehensions
- enumerate()
- Diccionarios
- Todo lo aprendido hoy
"""

ventas_laptops = [120, 340, 89, 230, 410]
ventas_mice = [25, 45, 30, 55, 40]
ventas_teclados = [67, 89, 45, 120, 95]


# Tu código aquí...

def calcular_total_ventas(ventas):
    return sum(ventas)


def calcular_venta_media(ventas):
    return calcular_total_ventas(ventas) / len(ventas)


def calcular_venta_maxima(ventas):
    return max(ventas)


def calcular_producto_del_dia(*productos, nombre_productos = None):
    """
    Encuentra el mejor día de ventas entre múltiples productos.

    Args:
        *productos: Múltiples listas de ventas (una por producto)

    Returns:
        Dict con información del mejor día
    """
    mejor_venta = 0
    mejor_dia = 0
    mejor_producto_index = 0

    # Recorrer cada lista de productos
    for productos_index, ventas in enumerate(productos):
        # Recorrer cada día de ese producto
        for dia, venta in enumerate(ventas, start=1):
            if venta > mejor_venta:
                mejor_venta = venta
                mejor_dia = dia
                mejor_producto_index = productos_index

    return {
        'producto': nombre_productos[mejor_producto_index],
        'dia': mejor_dia,
        'venta': mejor_venta
    }


resultado = calcular_producto_del_dia(
    ventas_laptops,
    ventas_mice,
    ventas_teclados,
    nombre_productos=["Laptops", "Ratones", "Teclados"]
)
print(resultado)
