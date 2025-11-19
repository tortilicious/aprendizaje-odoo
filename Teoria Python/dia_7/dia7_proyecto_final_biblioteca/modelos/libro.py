class Libro:
    """Modelo de Libro con Type Hints"""

    def __init__(
            self,
            id: int,
            titulo: str,
            autor: str,
            precio: float,
            disponible: bool = True,
            ano_publicacion: int = 2024) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.disponible = disponible
        self.ano_publicacion = ano_publicacion


    def __repr__(self) -> str:
        estado = "✅" if self.disponible else "❌"
        return f"Libro({self.titulo} - {self.autor}, ${self.precio} {estado})"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def marcar_disponible(self) -> None:
        self.disponible = True

    def marcar_no_disponible(self) -> None:
        self.disponible = False
