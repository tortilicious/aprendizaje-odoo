# Ejercicio 7 - Type hints con colecciones

from typing import List, Dict, Optional

# Función 1: Recibe lista de números, retorna el máximo
def encontrar_maximo(numeros: List[int]) -> int:
    return max(numeros) if numeros else None

# Función 2: Recibe diccionario, retorna lista de claves
def obtener_claves(datos: dict) -> list:
    return list(datos.keys())

# Función 3: Recibe lista de diccionarios (productos), retorna total de precios
def calcular_total_precios(productos: List[dict]) -> float:
    return sum(p["precio"] for p in productos)