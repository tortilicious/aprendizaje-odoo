from functools import wraps

# Ejercicio 6: Decorador cache simple
def con_cache(func):
    con_cache.cache_resultados = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Primero: busca en caché
        if args[0] in con_cache.cache_resultados:  # ← Primero mira
            print(f"💾 Resultado en caché para {args[0]}")
            return con_cache.cache_resultados[args[0]]

        # Si no está: ejecuta
        print(f"🔄 Calculando para {args[0]}")
        resultado = func(*args, **kwargs)

        # Guarda en caché
        con_cache.cache_resultados[args[0]] = resultado

        return resultado
    return wrapper


@con_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Calculando por primera vez:")
print(fibonacci(10))
print("\nResultado en caché:")
print(fibonacci(10))