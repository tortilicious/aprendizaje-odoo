from .libro import Libro

class Miembro:
    """Modelo de Miembro con Type Hints"""

    def __init__(self, id: int, nombre: str, email: str) -> None:
        self.id = id
        self.nombre = nombre
        self.email = email
        self.libros_prestados = []


    def __repr__(self) -> str:
        libros_miembro = ""
        if not self.libros_prestados:
            libros_miembro = "El miembro no tiene préstamos."
        else:
            for libro in self.libros_prestados:
                libros_miembro += f"\n  {libro.titulo}"
        return f"id: {self.id}, nombre: {self.nombre}, email: {self.email}\nlibros_prestados:\n{libros_miembro}"

    def prestar_libro(self, libro: Libro) -> None:
        if libro.disponible:
            self.libros_prestados.append(libro)
            print("Libro prestado con éxito.")
        else:
            print("El libro no se encuentra disponible.")

    def devolver_libro(self, libro: Libro) -> None:
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print("Libro devuelto con éxito.")
        else:
            print("El miembro no tiene ese libro prestado.")

    def cantidad_libros_pretados(self) -> int:
        if self.libros_prestados:
            return len(self.libros_prestados)
        return 0