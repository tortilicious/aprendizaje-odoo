# Ejercicio 9 - Type hynts con funciones complejas
"""
Crea una función que:

    Reciba una lista de libros (Libro objects)
    Reciba un criterio de búsqueda (lambda)
    Retorne una lista de libros que cumplen el criterio
"""


from typing import List, Callable
from ejercicio_8 import Libro

def filtrar_libros(libros: List[Libro], criterio: Callable[[Libro], bool]) -> List[Libro]:
    return list(filter(criterio, libros))


# Uso:
libros = [Libro(...), Libro(...), ...]

# Buscar libros disponibles
disponibles = filtrar_libros(libros, lambda libro: libro.disponible)

# Buscar libros baratos
baratos = filtrar_libros(libros, lambda libro: libro.precio < 30)