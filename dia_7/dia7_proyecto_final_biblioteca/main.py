from modelos.libro import Libro
from modelos.biblioteca import Biblioteca
from modelos.miembro import Miembro

def main() -> None:
    """Función principal que demuestra el sistema de biblioteca"""

    print("=" * 60)
    print("📚 SISTEMA DE BIBLIOTECA - DÍA 7")
    print("=" * 60)

    # ===== CREAR INSTANCIA DE BIBLIOTECA =====
    biblioteca = Biblioteca()

    # ===== CREAR LIBROS =====
    print("\n1️⃣  Creando libros...")
    libro1 = Libro(1, "1984", "George Orwell", 1200, True, 1949)
    libro2 = Libro(2, "Clean Code", "Robert Martin", 75, True, 2008)
    libro3 = Libro(3, "Python Pro", "Dan Bader", 45, True, 2021)
    libro4 = Libro(4, "The Pragmatic Programmer", "Hunt & Thomas", 55, True, 1999)
    libro5 = Libro(5, "Design Patterns", "Gang of Four", 89, True, 1994)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)
    biblioteca.agregar_libro(libro5)

    # ===== CREAR MIEMBROS =====
    print("\n2️⃣  Creando miembros...")
    miembro1 = Miembro(1, "Miguel", "miguel@email.com")
    miembro2 = Miembro(2, "Ana", "ana@email.com")
    miembro3 = Miembro(3, "Carlos", "carlos@email.com")

    biblioteca.agregar_miembro(miembro1)
    biblioteca.agregar_miembro(miembro2)
    biblioteca.agregar_miembro(miembro3)

    # ===== REALIZAR PRÉSTAMOS =====
    print("\n3️⃣  Realizando préstamos...")
    biblioteca.prestar_libro(1, 1)  # Miguel prestamo 1984
    biblioteca.prestar_libro(1, 2)  # Miguel prestamo Clean Code
    biblioteca.prestar_libro(2, 3)  # Ana prestamo Python Pro
    biblioteca.prestar_libro(3, 4)  # Carlos prestamo The Pragmatic Programmer

    # ===== OPERACIONES CON LAMBDA =====
    print("\n4️⃣  OPERACIONES CON LAMBDA:")
    print("-" * 60)

    print(f"\n💎 Libro más caro: {biblioteca.libro_mas_caro()}")
    print(f"💸 Libro más barato: {biblioteca.libro_mas_barato()}")

    print(f"\n📊 Libros ordenados por precio:")
    for libro in biblioteca.libros_ordenados_por_precio():
        print(f"  ${libro.precio:6} - {libro.titulo}")

    print(f"\n📅 Libros ordenados por año:")
    for libro in biblioteca.libros_ordenados_por_ano():
        print(f"  {libro.ano_publicacion} - {libro.titulo}")

    miembro_top = biblioteca.miembro_que_mas_libros_prestados()
    print(f"\n👑 Miembro con más libros: {miembro_top.nombre} ({len(miembro_top.libros_prestados)} libros)")

    # ===== OPERACIONES CON LIST COMPREHENSION =====
    print("\n5️⃣  OPERACIONES CON LIST COMPREHENSION:")
    print("-" * 60)

    disponibles = biblioteca.libros_disponibles()
    print(f"\n✅ Libros disponibles ({len(disponibles)}):")
    for libro in disponibles:
        print(f"  - {libro.titulo}")

    no_disponibles = biblioteca.libros_no_disponibles()
    print(f"\n❌ Libros NO disponibles ({len(no_disponibles)}):")
    for libro in no_disponibles:
        print(f"  - {libro.titulo}")

    libros_orwell = biblioteca.libros_de_autor("George Orwell")
    print(f"\n📖 Libros de George Orwell ({len(libros_orwell)}):")
    for libro in libros_orwell:
        print(f"  - {libro.titulo}")

    libros_viejos = biblioteca.libros_anteriores(2000)
    print(f"\n📜 Libros anteriores a 2000 ({len(libros_viejos)}):")
    for libro in libros_viejos:
        print(f"  - {libro.titulo} ({libro.ano_publicacion})")

    sin_libros = biblioteca.miembros_sin_libros()
    print(f"\n👤 Miembros sin libros prestados ({len(sin_libros)}):")
    for miembro in sin_libros:
        print(f"  - {miembro.nombre}")

    # ===== DEVOLUCIONES =====
    print("\n6️⃣  Devolviendo libros...")
    biblioteca.devolver_libro(1, 1)  # Miguel devuelve 1984
    print(f"Miguel devolvió 1984")

    # ===== REPORTES =====
    print("\n7️⃣  REPORTES FINALES:")
    biblioteca.estadisticas()


if __name__ == "__main__":
    main()