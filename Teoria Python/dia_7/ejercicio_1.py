#  Ejercicio 1 - Lambda básica con sorted()
"""
Crea un programa que:

Ordene por edad (de menor a mayor)
Ordene por nombre (alfabéticamente)
Ordene por edad (de mayor a menor)

Usa lambda con sorted() en cada caso.
"""

personas = [("Miguel", 25), ("Ana", 30), ("Carlos", 22), ("Diana", 28)]

personas_por_edad = sorted(personas, key=lambda x: x[1])
# print(personas_por_edad)

personas_por_nombre = sorted(personas, key=lambda x: x[0])
# print(personas_por_nombre)

personas_por_edad_inverso = sorted(personas, key=lambda x: x[1], reverse=True)
print(personas_por_edad_inverso)