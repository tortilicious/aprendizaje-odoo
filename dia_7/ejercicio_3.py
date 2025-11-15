# Ejercicio 3 - Lambda con diccionarios

"""
Ordena por precio (de menor a mayor)
Encuentra el producto más caro (max + lambda)
Encuentra el producto con más stock (max + lambda)
Ordena por nombre (alfabéticamente)
"""

productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 50},
    {"nombre": "Teclado", "precio": 75, "stock": 0},
    {"nombre": "Monitor", "precio": 300, "stock": 10},
]

productos_por_precio = sorted(productos, key=lambda x: x["precio"])
# print(productos_por_precio)

producto_mas_caro = max(productos, key=lambda x: x["precio"])
# print(producto_mas_caro)

producto_con_mayor_stock = max(productos, key=lambda produdcto: produdcto["stock"])
# print(producto_con_mayor_stock)

productos_ordenados_alfabeticamente = sorted(productos, key=lambda producto: producto["nombre"])
print(productos_ordenados_alfabeticamente)