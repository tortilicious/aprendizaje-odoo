# Ejercicio 2 - Lambda con max() y min()

"""
La persona más joven (usa min() con lambda)
La persona más vieja (usa max() con lambda)
La persona cuyo nombre es más largo (usa max() con lambda en len(nombre))
"""

personas = [("Miguel", 25), ("Ana", 30), ("Carlos", 22), ("Diana", 28)]

persona_mas_joven = min(personas, key=lambda x: x[1])
# print(persona_mas_joven)

persona_mas_vieja = max(personas, key=lambda x: x[1])
# print(persona_mas_vieja)

persona_nombre_mas_largo = max(personas, key=lambda x: len(x[0]))
print(persona_nombre_mas_largo)