from typing import List, Optional
from .libro import Libro
from .miembro import Miembro


class Biblioteca:
    """Modelo de biblioteca"""

    def __init__(self) -> None:
        self.libros = []
        self.miembros = []

    # ===== MÉTODOS BÁSICOS =====

    def agregar_miembro(self, miembro: Miembro) -> None:
        if miembro not in self.miembros:
            self.miembros.append(miembro)
            print("Agregado nuevo miembro a la biblioteca.")
        else:
            print("El miembro ya existe a la biblioteca.")

    def agregar_libro(self, libro: Libro) -> None:
        if libro not in self.libros:
            self.libros.append(libro)
            print("Libro agregado a la biblioteca.")
        else:
            print("El libro ya se encuentra en la biblioteca.")

    def buscar_miembro(self, miembro_id: int) -> Optional[Miembro]:
        for miembro in self.miembros:
            if miembro.id == miembro_id:
                return miembro
        return None

    def buscar_libro(self, libro_id: int) -> Optional[Libro]:
        for libro in self.libros:
            if libro.id == libro_id:
                return libro
        return None

    # ===== OPERACIONES CON LAMBDA =====

    def libro_mas_caro(self) -> Optional[Libro]:
        if self.libros:
            return max(self.libros, key=lambda libro: libro.precio)
        return None

    def libro_mas_barato(self) -> Optional[Libro]:
        if self.libros:
            return min(self.libros, key=lambda libro: libro.precio)
        return None

    def libros_ordenados_por_precio(self) -> List[Libro]:
        return sorted(self.libros, key=lambda libro: libro.precio)


    def libros_ordenados_por_ano(self) -> List[Libro]:
        return sorted(self.libros, key=lambda libro: libro.ano_publicacion)


    def miembro_que_mas_libros_prestados(self) -> Optional[Miembro]:
        if self.miembros:
            return max(self.miembros, key=lambda miembro: len(miembro.libros_prestados))
        return None

    # ===== OPERACIONES CON LIST COMPREHENSION =====

    def libros_disponibles(self) -> List[Libro]:
        return [libro for libro in self.libros if libro.disponible]

    def libros_no_disponibles(self) -> List[Libro]:
        return [libro for libro in self.libros if not libro.disponible]


    def libros_de_autor(self, autor: str) -> List[Libro]:
        return [libro for libro in self.libros if libro.autor == autor]


    def libros_anteriores(self, ano_publicacion: int) -> List[Libro]:
        return [libro for libro in self.libros if libro.ano_publicacion < ano_publicacion]

    def miembros_sin_libros(self) -> List[Miembro]:
        return [miembro for miembro in self.miembros if not miembro.libros_prestados]

    # ===== OPERACIONES DE PRÉSTAMO =====

    def prestar_libro(self, miembro_id: int, libro_id: int) -> bool:
        miembro = self.buscar_miembro(miembro_id)
        libro = self.buscar_libro(libro_id)

        if miembro and libro and libro.disponible:
            miembro.libros_prestados.append(libro)
            libro.marcar_no_disponible()
            return True

        return False

    def devolver_libro(self, miembro_id: int, libro_id: int) -> bool:
        miembro = self.buscar_miembro(miembro_id)
        libro = self.buscar_libro(libro_id)
        if miembro and libro and libro in miembro.libros_prestados:
            miembro.libros_prestados.remove(libro)
            libro.marcar_disponible()
            return True

        return False

    # ===== REPORTES =====

    def reporte_inventario(self) -> None:
        print("Libros ordenados por precio:\n")
        libros_por_precio = self.libros_ordenados_por_precio()
        for libro in libros_por_precio:
            print(libro.__repr__())

    def reporte_miembros(self) -> None:
        print("Miembros ordenados por préstamos:\n")
        miembros_por_prestamos = sorted(self.miembros, key=lambda miembro: miembro.cantidad_libros_pretados())
        for miembro in miembros_por_prestamos:
            print(miembro.__repr__())

    def estadisticas(self) -> None:
        """Imprime estadísticas generales de la biblioteca"""
        print("\n" + "=" * 60)
        print("📊 ESTADÍSTICAS DE LA BIBLIOTECA")
        print("=" * 60)
        print(f"Total de libros: {len(self.libros)}")
        print(f"Total de miembros: {len(self.miembros)}")
        print(f"Libros disponibles: {len(self.libros_disponibles())}")
        print(f"Libros prestados: {len(self.libros_no_disponibles())}")
        print(f"Total de préstamos activos: {sum(len(m.libros_prestados) for m in self.miembros)}")

        if self.libros:
            print(f"Libro más caro: {self.libro_mas_caro().titulo} (${self.libro_mas_caro().precio})")
            print(f"Libro más barato: {self.libro_mas_barato().titulo} (${self.libro_mas_barato().precio})")

        if self.miembros:
            miembro_top = self.miembro_que_mas_libros_prestados()
            print(f"Miembro con más libros: {miembro_top.nombre} ({len(miembro_top.libros_prestados)} libros)")

        print("=" * 60 + "\n")

