# Ejercicio 3 - Agrupar por categoria

productos = [
    {'nombre': 'Laptop', 'categoria': 'Electrónica', 'precio': 1200},
    {'nombre': 'Mouse', 'categoria': 'Accesorios', 'precio': 20},
    {'nombre': 'Monitor', 'categoria': 'Electrónica', 'precio': 300},
    {'nombre': 'Teclado', 'categoria': 'Accesorios', 'precio': 80},
]

def agrupar_por_categoria(productos):
    # TODO: Agrupa productos por categoría
    # Retorna: {'Electrónica': [...], 'Accesorios': [...]}
    diccionario_categoria = {}

    for producto in productos:
        categoria = producto['categoria']

        if categoria not in diccionario_categoria:
            diccionario_categoria[categoria] = []

        diccionario_categoria[categoria].append(producto)
    return diccionario_categoria

# Prueba:
resultado = agrupar_por_categoria(productos)
print(resultado)