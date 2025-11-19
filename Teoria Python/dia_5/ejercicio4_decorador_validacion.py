"""
Crea un decorador llamado validar_rango que
 acepte dos parámetros: minimo y maximo
"""
from functools import wraps


def validar_rango(minimo, maximo):
    def decorador_real(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            if resultado not in range(minimo, maximo):
                raise ValueError(f"Resultado {resultado} fuera de rango [{minimo}, {maximo}]")
            return resultado

        return wrapper

    return decorador_real


@validar_rango(0, 100)
def calcular_descuento(precio):
    """Descuento debe estar entre 0 y 100%"""
    return precio * 0.5


descuento = calcular_descuento(100)
print(descuento)

try:
    descuento = calcular_descuento(1000)
    print(descuento)
except ValueError as e:
    print(f"Error: {e}")


@validar_rango(0, 130)
def calcular_edad(ano_nacimiento):
    return 2025 - ano_nacimiento

try:
    edad = calcular_edad(1102)
    print(f"Edad: {edad} años.")
except ValueError as e:
    print(f"Error: {e}")