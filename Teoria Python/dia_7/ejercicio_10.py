# Ejercicio 10 - Type Hints con Dict Complejos

from typing import Dict, List


def obtener_estadisticas(productos: Dict[str, Dict]) -> Dict[str, any]:
    """
    Recibe un diccionario como:
    {
        "Laptop": {"precio": 1200, "stock": 5},
        "Mouse": {"precio": 25, "stock": 50},
    }

    Retorna un diccionario con:
    {
        "producto_mas_caro": "Laptop",
        "producto_mas_barato": "Mouse",
        "precio_promedio": 612.5,
        "stock_total": 55
    }
    """
    return {
        "producto_mas_caro": max(productos.items(), key=lambda x: x["precio"])
    }