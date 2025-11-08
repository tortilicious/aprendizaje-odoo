from functools import wraps
import time
import random

# Decorador de Reintentos

def reintentar(max_intentos = 3, espera = 1.0):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(1, max_intentos + 1):
                try:
                    print(f"Intento {intento}/{max_intentos}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if intento == max_intentos:
                        print(f"El programa no ha podido ejecutarse: {e}")
                        raise
                    print(f"Intento {intento} falló: {e}. Reintentando en {espera}s...")
                    time.sleep(espera)
        return wrapper
    return decorador


@reintentar(max_intentos=3, espera=0.5)
def conectar_servidor():
    if random.random() < 0.7:
        raise ConnectionError("Servidor no disponible")
    return "Conectado"

try:
    print(conectar_servidor())
except ConnectionError as e:
    print(f"Error: {e}")