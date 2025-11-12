def contar_hasta(n):
    for i in range(1, n + 1):
        print(f"Generando {i}")
        yield i


# El for llama a next() automáticamente en cada iteración
for numero in contar_hasta(3):
    print(f"Recibí: {numero}")
