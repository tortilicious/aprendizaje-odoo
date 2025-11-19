# Ejercicio 5 - Lambda en map() vs List Comprehension

"""
Haz lo siguiente DE DOS FORMAS (lambda + map vs list comprehension):

    Duplica cada número
    Filtra solo los pares
    Convierte a strings
"""

numeros = [1, 2, 3, 4, 5]


# Numeros duplicados
numeros_duplicados_lambda = list(map(lambda x: x * 2, numeros))
print(numeros_duplicados_lambda)

numeros_duplicados_comprehension = [num * 2 for num in numeros]
print(numeros_duplicados_comprehension)

# Filtrar pares
numeros_pares_lambda = list(filter(lambda x: x%2 == 0, numeros))
print(numeros_pares_lambda)

numeros_pares_comprehension = [num for num in numeros if num % 2 == 0]
print(numeros_pares_comprehension)


# Convertir a strings
numeros_string_lambda = list(map(lambda x: str(x), numeros))
print(numeros_string_lambda)

numeros_string_comprehension = [str(num) for num in numeros]
print(numeros_string_comprehension)


