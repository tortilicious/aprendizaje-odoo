# Ejercicio 4 - Lambda con Callback

"""
Crea una función llamada aplicar_operacion que reciba:

    Una lista de números
    Una lambda (callback) que haga algo con esos números

Crea 3 usos diferentes:

    Multiplicar cada número por 3 (usa lambda)
    Elevar cada número al cuadrado (usa lambda)
    Filtrar solo números mayores a 10 (usa lambda)
"""
from typing import Collection, Callable

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def aplicar_operacion(lista_numeros: list, operacion: Callable[[int], int]) -> list :
    return list(map(operacion, lista_numeros))

# Multiplicar por 3
resultado1 = aplicar_operacion(numeros, lambda numero: numero * 3)
print(resultado1)

# Elevar al cuadrado
resultado2 = aplicar_operacion(numeros, lambda numero: numero * numero)
print(resultado2)

# Filtrar mayores a 10
resultado3 = aplicar_operacion(numeros, lambda numero: numero > 10)
print(resultado3)