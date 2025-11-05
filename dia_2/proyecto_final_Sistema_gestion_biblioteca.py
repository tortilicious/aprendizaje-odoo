"""
PROYECTO FINAL DÍA 2: Sistema de Gestión de Biblioteca - VERSIÓN CORREGIDA

Correcciones aplicadas:
1. Cliente: Inicialización correcta de _prestamos_activos
2. Cliente: Añadido __str__ y __eq__
3. Cliente: devolver_libro() elimina préstamo de la lista
4. Libro: Separado __str__ y __repr__
5. Biblioteca: prestar_libro() retorna True
6. Biblioteca: Añadido generar_reporte()
7. Biblioteca: Añadido listar_prestamos_activos() y listar_prestamos_retrasados()
8. Prestamo: dias_retraso considera si está devuelto
"""

from datetime import datetime, timedelta


class Libro:
    """
    Representa un libro en la biblioteca.
    """

    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"Libro: {self.titulo} por {self.autor}"

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', isbn='{self.isbn}')"

    def __eq__(self, otro_libro):
        return self.isbn == otro_libro.isbn


class Cliente:
    """
    Representa un cliente de la biblioteca.
    """

    def __init__(self, nombre, email, prestamos_activos=None):
        self.nombre = nombre
        self.email = email
        self._prestamos_activos = prestamos_activos or []  # ✅ Corregido

    @property
    def prestamos_activos(self):
        return self._prestamos_activos

    @property
    def tiene_prestamos(self):
        return len(self._prestamos_activos) > 0

    def agregar_prestamo(self, prestamo):
        self._prestamos_activos.append(prestamo)

    def devolver_libro(self, libro):
        for prestamo in self._prestamos_activos:
            if prestamo.libro == libro:
                prestamo.marcar_como_devuelto()
                libro.disponible = True
                self._prestamos_activos.remove(prestamo)  # ✅ Eliminar de lista
                return

    def __str__(self):  # ✅ Añadido
        n_prestamos = len(self._prestamos_activos)
        return f"Cliente: {self.nombre} ({self.email}) - {n_prestamos} préstamos activos"

    def __eq__(self, otro):  # ✅ Añadido
        return self.email == otro.email


class Prestamo:
    """
    Representa un préstamo de un libro a un cliente.
    """

    DIAS_PRESTAMO = 7
    MULTA_POR_DIA = 2.0

    def __init__(self, libro, cliente):
        self.libro = libro
        self.cliente = cliente
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        self.devuelto = False

    def __str__(self):
        fecha_devolucion_string = self.fecha_devolucion.strftime("%d/%m/%Y")
        return f"{self.libro.titulo} prestado a {self.cliente.nombre} - Debe devolver: {fecha_devolucion_string}"

    @property
    def esta_retrasado(self):
        return datetime.now() > self.fecha_devolucion

    @property
    def dias_retraso(self):
        if self.devuelto:  # ✅ Corregido - considerar si está devuelto
            return 0
        if self.esta_retrasado:
            return (datetime.now() - self.fecha_devolucion).days
        return 0

    @property
    def multa(self):
        return self.MULTA_POR_DIA * self.dias_retraso

    def marcar_como_devuelto(self):
        self.devuelto = True


class Biblioteca:
    """
    Sistema principal que coordina libros, clientes y préstamos.
    """

    def __init__(self, nombre, libros=None, clientes=None, prestamos=None):
        self.nombre = nombre
        self.libros = libros or []
        self.clientes = clientes or []
        self.prestamos = prestamos or []

    def agregar_libro(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)

    def agregar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)

    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_cliente_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente
        return None

    def prestar_libro(self, isbn, email_cliente):
        libro = self.buscar_libro_por_isbn(isbn)
        if libro is None or not libro.disponible:  # ✅ Simplificado
            return False

        cliente = self.buscar_cliente_por_email(email_cliente)
        if cliente is None:
            return False

        prestamo = Prestamo(libro, cliente)
        cliente.agregar_prestamo(prestamo)
        self.prestamos.append(prestamo)  # ✅ Guardar en biblioteca también
        libro.disponible = False
        return True  # ✅ Retornar True

    def devolver_libro(self, isbn, email_cliente):
        cliente = self.buscar_cliente_por_email(email_cliente)
        if cliente is None:
            return 0

        for prestamo in cliente.prestamos_activos:
            if prestamo.libro.isbn == isbn:
                multa = prestamo.multa
                prestamo.marcar_como_devuelto()
                libro = prestamo.libro
                libro.disponible = True
                cliente.prestamos_activos.remove(prestamo)  # ✅ Eliminar de lista
                return multa
        return 0

    def listar_prestamos_activos(self):  # ✅ Añadido
        return [p for p in self.prestamos if not p.devuelto]

    def listar_prestamos_retrasados(self):  # ✅ Añadido
        return [p for p in self.prestamos if p.esta_retrasado and not p.devuelto]

    def generar_reporte(self):  # ✅ Añadido
        print(f"📊 REPORTE - {self.nombre}")
        print("-" * 50)
        print(f"Total de libros: {len(self.libros)}")
        print(f"Total de clientes: {len(self.clientes)}")
        print(f"Préstamos totales: {len(self.prestamos)}")
        print(f"Préstamos activos: {len(self.listar_prestamos_activos())}")
        print(f"Préstamos retrasados: {len(self.listar_prestamos_retrasados())}")


# ============================================================================
# TESTS
# ============================================================================

def test_sistema_biblioteca():
    """Tests completos del sistema"""
    print("🧪 Ejecutando tests del Proyecto Final...\n")
    print("=" * 70)

    # Setup inicial
    print("\n📚 SETUP: Creando biblioteca y datos iniciales\n")
    biblioteca = Biblioteca("Biblioteca Municipal")

    # Crear libros
    libro1 = Libro("1984", "George Orwell", "978-0-452-28423-4")
    libro2 = Libro("El Quijote", "Cervantes", "978-84-376-0494-7")
    libro3 = Libro("Cien años de soledad", "García Márquez", "978-0-06-088328-7")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    print(f"✅ {len(biblioteca.libros)} libros agregados al catálogo\n")

    # Crear clientes
    cliente1 = Cliente("Ana López", "ana@email.com")
    cliente2 = Cliente("Luis García", "luis@email.com")

    biblioteca.agregar_cliente(cliente1)
    biblioteca.agregar_cliente(cliente2)
    print(f"✅ {len(biblioteca.clientes)} clientes registrados\n")

    # Test 1: Préstamo exitoso
    print("=" * 70)
    print("\n📖 TEST 1: Préstamo exitoso\n")
    exito = biblioteca.prestar_libro("978-0-452-28423-4", "ana@email.com")
    assert exito == True, "❌ El préstamo debería ser exitoso"
    assert libro1.disponible == False, "❌ El libro debería estar no disponible"
    assert len(cliente1.prestamos_activos) == 1, "❌ Cliente debería tener 1 préstamo"
    print(f"✅ Préstamo exitoso: {libro1.titulo} → {cliente1.nombre}")
    print(f"   Libro disponible: {libro1.disponible}")
    print(f"   Préstamos de {cliente1.nombre}: {len(cliente1.prestamos_activos)}\n")

    # Test 2: No se puede prestar libro no disponible
    print("=" * 70)
    print("\n🚫 TEST 2: Intentar prestar libro ya prestado\n")
    exito = biblioteca.prestar_libro("978-0-452-28423-4", "luis@email.com")
    assert exito == False, "❌ No debería poder prestar un libro no disponible"
    print(f"✅ Préstamo rechazado correctamente (libro no disponible)\n")

    # Test 3: Múltiples préstamos a un cliente
    print("=" * 70)
    print("\n📚 TEST 3: Múltiples préstamos a un cliente\n")
    biblioteca.prestar_libro("978-84-376-0494-7", "ana@email.com")
    assert len(cliente1.prestamos_activos) == 2, "❌ Cliente debería tener 2 préstamos"
    print(f"✅ Cliente {cliente1.nombre} tiene {len(cliente1.prestamos_activos)} préstamos activos\n")

    # Test 4: Devolución sin retraso
    print("=" * 70)
    print("\n✅ TEST 4: Devolución sin retraso (sin multa)\n")
    multa = biblioteca.devolver_libro("978-84-376-0494-7", "ana@email.com")
    assert multa == 0, "❌ No debería haber multa si se devuelve a tiempo"
    assert libro2.disponible == True, "❌ El libro debería estar disponible de nuevo"
    assert len(cliente1.prestamos_activos) == 1, "❌ Cliente debería tener 1 préstamo activo"
    print(f"✅ Devolución exitosa sin multa")
    print(f"   Libro disponible: {libro2.disponible}")
    print(f"   Préstamos activos de {cliente1.nombre}: {len(cliente1.prestamos_activos)}\n")

    # Test 5: Simulación de retraso y multa
    print("=" * 70)
    print("\n⏰ TEST 5: Simulación de retraso con multa\n")
    # Forzar fecha de préstamo antigua para simular retraso
    prestamo_activo = cliente1.prestamos_activos[0]
    prestamo_activo.fecha_prestamo = datetime.now() - timedelta(days=15)
    prestamo_activo.fecha_devolucion = prestamo_activo.fecha_prestamo + timedelta(days=7)

    dias_retraso = prestamo_activo.dias_retraso
    multa_esperada = prestamo_activo.multa
    print(f"   Días de retraso: {dias_retraso}")
    print(f"   Multa calculada: {multa_esperada}€")

    assert dias_retraso > 0, "❌ Debería haber días de retraso"
    assert multa_esperada > 0, "❌ Debería haber multa"

    multa_devolucion = biblioteca.devolver_libro("978-0-452-28423-4", "ana@email.com")
    assert multa_devolucion == multa_esperada, "❌ La multa no coincide"
    print(f"✅ Multa aplicada correctamente: {multa_devolucion}€\n")

    # Test 6: Métodos especiales
    print("=" * 70)
    print("\n🔍 TEST 6: Métodos especiales (__str__, __eq__)\n")

    print(f"str(libro1): {libro1}")
    print(f"repr(libro1): {repr(libro1)}")
    print(f"str(cliente1): {cliente1}")

    libro_duplicado = Libro("Otro título", "Otro autor", "978-0-452-28423-4")
    assert libro1 == libro_duplicado, "❌ Libros con mismo ISBN deberían ser iguales"
    print(f"✅ Igualdad de libros por ISBN funciona correctamente\n")

    # Test 7: Reporte general
    print("=" * 70)
    print("\n📊 TEST 7: Reporte general de la biblioteca\n")
    biblioteca.generar_reporte()

    print("\n" + "=" * 70)
    print("\n🎉 ¡TODOS LOS TESTS PASARON! Sistema completo funcionando.\n")
    print("=" * 70)


if __name__ == "__main__":
    test_sistema_biblioteca()