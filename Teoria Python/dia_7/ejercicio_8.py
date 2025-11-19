# Ejercicio 8 - Type hints en clases

class Libro:
    # Atributos: id (int), titulo (str), autor (str), precio (float), disponible (bool)

    def __init__(self, id: int, titulo: str, autor: str, precio: float, disponible: bool =True):
        self.id: int = id
        self.titulo: str = titulo
        self.autor: str = autor
        self.precio: float = precio
        self.disponible: bool = disponible
        pass

    def obtener_info(self) -> str:
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: {self.precio}"


    def cambiar_disponibilidad(self, disponible: bool) -> None:
        self.disponible = disponible


    def aplicar_descuento(self, porcentaje: float) -> float:
        return self.precio * porcentaje
