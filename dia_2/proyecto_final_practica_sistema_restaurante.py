"""
PROYECTO EXTRA: Sistema de Gestión de Restaurante

Objetivo: Practicar POO con un contexto diferente a la biblioteca

CONCEPTOS QUE PRACTICARÁS:
✅ Clases básicas con constructor
✅ Métodos especiales (__str__, __repr__, __eq__)
✅ Propiedades (@property) con cálculos
✅ Composición entre clases
✅ Lógica de negocio (descuentos, totales, propinas)
✅ Gestión de listas y búsquedas

REQUISITOS DEL SISTEMA:
1. Gestionar platos del menú (nombre, precio, categoría, disponible)
2. Gestionar clientes (nombre, email, puntos de fidelidad)
3. Gestionar pedidos (cliente, platos, estado, propina)
4. Calcular totales con descuentos según puntos
5. Sistema de puntos: cada 10€ gastados = 1 punto
6. Descuentos: 50 puntos = 5€, 100 puntos = 15€, 200 puntos = 35€
"""
from datetime import datetime


class Plato:
    """
        Representa un plato del menú.

        Atributos:
            nombre (str): Nombre del plato
            precio (float): Precio del plato
            categoria (str): Categoría (entrante, principal, postre, bebida)
            disponible (bool): Sí está disponible para pedir

        Métodos especiales:
            __str__: "Plato: [nombre] - [precio]€ ([categoría])"
            __repr__: "Plato(nombre='...', precio=..., categoria='...')"
            __eq__: Dos platos son iguales si tienen el mismo nombre
        """

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = True

    def __str__(self):
        return f"Plato: {self.nombre} - {self.precio}€ ({self.categoria})"

    def __repr__(self):
        return f"Plato(nombre='{self.nombre}', precio={self.precio}, categoria='{self.categoria}')"

    def __eq__(self, otro_plato):
        return self.nombre == otro_plato.nombre


class Cliente:
    """
       Representa un cliente del restaurante.

       Atributos:
           nombre (str): Nombre del cliente
           email (str): Email único
           _puntos (int): Puntos de fidelidad acumulados (privado)
           _pedidos (list): Lista de pedidos realizados (privado)

       Propiedades:
           puntos: Getter para puntos (solo lectura)
           pedidos: Getter para pedidos (solo lectura)
           total_gastado: Suma de todos los totales de pedidos completados
           nivel_fidelidad: "Bronce" (<50 pts), "Plata" (50-99), "Oro" (100-199), "Platino" (200+)

       Métodos:
           agregar_puntos(cantidad): Añade puntos
           usar_puntos(cantidad): Resta puntos (retorna True si se pudo, False si no hay suficientes)
           agregar_pedido(pedido): Añade un pedido a la lista

       Métodos especiales:
           __str__: "Cliente: [nombre] - [puntos] puntos ([nivel])"
           __eq__: Iguales si tienen el mismo email
       """

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self._puntos = 0
        self._pedidos = []

    def __str__(self):
        return f"Cliente: {self.nombre} - {self.puntos} puntos ({self.nivel_fidelidad})"

    def __eq__(self, otro_cliente):
        return self.email == otro_cliente.email

    @property
    def puntos(self):
        return self._puntos

    @property
    def pedidos(self):
        return self._pedidos

    @property
    def total_gastado(self):
        return sum(pedido.total for pedido in self._pedidos if pedido.estado == "completado")

    @property
    def nivel_fidelidad(self):
        if self.puntos < 50:
            return "Bronce"
        elif 50 <= self.puntos < 100:
            return "Plata"
        elif 100 <= self.puntos < 200:
            return "Oro"
        else:
            return "Platino"

    def agregar_puntos(self, puntos):
        self._puntos += puntos

    def usar_puntos(self, puntos):
        if self.puntos >= puntos:
            self._puntos -= puntos
            return True
        return False

    def agregar_pedido(self, pedido):
        self._pedidos.append(pedido)


class Pedido:
    """
    Representa un pedido de un cliente.
    """

    DESCUENTOS = {
        50: 5.0,  # 50 puntos = 5€ descuento
        100: 15.0,  # 100 puntos = 15€ descuento
        200: 35.0  # 200 puntos = 35€ descuento
    }

    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []
        self.fecha = datetime.now()
        self.estado = "pendiente"  # ✅ Minúscula
        self._propina = 0.0
        self._descuento_aplicado = 0.0

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - {len(self.platos)} platos - Total: {self.total}€ ({self.estado})"

    @property
    def propina(self):
        return self._propina

    @propina.setter  # ✅ Correcto
    def propina(self, valor):
        if valor < 0:
            raise ValueError("La propina no puede ser negativa")
        self._propina = valor

    @property
    def descuento_aplicado(self):
        return self._descuento_aplicado  # ✅ Retorna el valor, no bool

    @property
    def subtotal(self):
        return sum(plato.precio for plato in self.platos)

    @property
    def total(self):
        return self.subtotal - self._descuento_aplicado + self._propina

    def agregar_plato(self, plato):
        if plato.disponible and self.estado == "pendiente":  # ✅ Minúscula
            self.platos.append(plato)

    def aplicar_descuento_puntos(self, cliente):  # ✅ Nombre correcto
        """
        Aplica descuento según puntos del cliente.

        Returns:
            float: Descuento aplicado en euros
        """
        descuento = 0.0
        puntos_a_usar = 0

        if cliente.puntos >= 200:
            descuento = self.DESCUENTOS[200]
            puntos_a_usar = 200
        elif cliente.puntos >= 100:
            descuento = self.DESCUENTOS[100]
            puntos_a_usar = 100
        elif cliente.puntos >= 50:
            descuento = self.DESCUENTOS[50]
            puntos_a_usar = 50

        if puntos_a_usar > 0:
            cliente.usar_puntos(puntos_a_usar)
            self._descuento_aplicado = descuento

        return descuento  # ✅ Siempre retorna

    def completar(self):
        self.estado = "completado"  # ✅ Minúscula
        puntos_ganados = int(self.total / 10)  # ✅ Usar total, no subtotal
        self.cliente.agregar_puntos(puntos_ganados)

    def cancelar(self):
        self.estado = "cancelado"  # ✅ Minúscula

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []
        self.clientes = []
        self.pedidos = []

    def agregar_plato(self, plato):
        if plato not in self.menu:
            self.menu.append(plato)

    def agregar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)

    def buscar_plato_por_nombre(self, nombre_plato):
        for plato in self.menu:
            if plato.nombre == nombre_plato:
                return plato
        return None

    def buscar_cliente_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente
        return None

    def crear_pedido(self, email_cliente):
        cliente = self.buscar_cliente_por_email(email_cliente)
        if cliente is not None:
            pedido = Pedido(cliente)
            self.pedidos.append(pedido)
            cliente.agregar_pedido(pedido)
            return pedido
        return None

    def listar_platos_por_categoria(self, categoria):
        return [plato for plato in self.menu if plato.categoria == categoria]

    def listar_pedidos_pendientes(self):
        return [pedido for pedido in self.pedidos if pedido.estado == "pendiente"]

    def listar_pedidos_completados(self):
        return [pedido for pedido in self.pedidos if pedido.estado == "completado"]

    def calcular_ingresos_totales(self):
        return sum(pedido.total for pedido in self.pedidos if pedido.estado == "completado")

    def cliente_mas_frecuente(self):
        if not self.clientes:
            return None
        return max(self.clientes, key=lambda cliente: len([pedido for pedido in cliente.pedidos if pedido.estado == "completado"]))

    def generar_reporte(self):
        print(f"📊 REPORTE - {self.nombre}")
        print("-" * 50)
        print(f"Platos en menú: {len(self.menu)}")
        print(f"Clientes registrados: {len(self.clientes)}")
        print(f"Pedidos totales: {len(self.pedidos)}")
        print(f"Pedidos completados: {len(self.listar_pedidos_completados())}")
        print(f"Ingresos totales: {self.calcular_ingresos_totales()}€")

        cliente_top = self.cliente_mas_frecuente()
        if cliente_top:
            pedidos_completados = len([p for p in cliente_top.pedidos if p.estado == "completado"])
            print(f"Cliente más frecuente: {cliente_top.nombre} ({pedidos_completados} pedidos)")


def test_sistema_restaurante():
    """Tests completos del sistema"""
    print("🧪 Ejecutando tests del Sistema de Restaurante...\n")
    print("=" * 70)

    # Setup inicial
    print("\n🍽️  SETUP: Creando restaurante y datos iniciales\n")
    restaurante = Restaurante("La Buena Mesa")

    # Crear platos
    plato1 = Plato("Ensalada César", 8.50, "entrante")
    plato2 = Plato("Pizza Margherita", 12.00, "principal")
    plato3 = Plato("Tiramisú", 6.00, "postre")
    plato4 = Plato("Agua", 2.00, "bebida")
    plato5 = Plato("Pasta Carbonara", 14.00, "principal")

    restaurante.agregar_plato(plato1)
    restaurante.agregar_plato(plato2)
    restaurante.agregar_plato(plato3)
    restaurante.agregar_plato(plato4)
    restaurante.agregar_plato(plato5)
    print(f"✅ {len(restaurante.menu)} platos agregados al menú\n")

    # Crear clientes
    cliente1 = Cliente("Ana López", "ana@email.com")
    cliente2 = Cliente("Luis García", "luis@email.com")

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    print(f"✅ {len(restaurante.clientes)} clientes registrados\n")

    # Test 1: Crear pedido y añadir platos
    print("=" * 70)
    print("\n📝 TEST 1: Crear pedido y añadir platos\n")
    pedido1 = restaurante.crear_pedido("ana@email.com")
    assert pedido1 is not None, "❌ El pedido debería crearse correctamente"
    assert pedido1.cliente == cliente1, "❌ El pedido debería ser del cliente correcto"

    pedido1.agregar_plato(plato1)
    pedido1.agregar_plato(plato2)
    pedido1.agregar_plato(plato4)

    assert len(pedido1.platos) == 3, "❌ El pedido debería tener 3 platos"
    print(f"✅ Pedido creado con {len(pedido1.platos)} platos")
    print(f"   Subtotal: {pedido1.subtotal}€\n")

    # Test 2: Calcular total con propina
    print("=" * 70)
    print("\n💰 TEST 2: Calcular total con propina\n")
    pedido1.propina = 2.50
    subtotal = pedido1.subtotal
    total = pedido1.total

    assert subtotal == 22.50, f"❌ Subtotal debería ser 22.50€, es {subtotal}€"
    assert total == 25.00, f"❌ Total debería ser 25.00€ (22.50 + 2.50), es {total}€"
    print(f"✅ Subtotal: {subtotal}€")
    print(f"   Propina: {pedido1.propina}€")
    print(f"   Total: {total}€\n")

    # Test 3: Completar pedido y ganar puntos
    print("=" * 70)
    print("\n⭐ TEST 3: Completar pedido y ganar puntos\n")
    pedido1.completar()

    assert pedido1.estado == "completado", "❌ El estado debería ser 'completado'"
    puntos_ganados = int(pedido1.total / 10)  # 25€ / 10 = 2 puntos
    assert cliente1.puntos == puntos_ganados, f"❌ Cliente debería tener {puntos_ganados} puntos"
    print(f"✅ Pedido completado")
    print(f"   Puntos ganados: {cliente1.puntos}")
    print(f"   Nivel: {cliente1.nivel_fidelidad}\n")

    # Test 4: Crear segundo pedido para acumular puntos
    print("=" * 70)
    print("\n🎯 TEST 4: Acumular más puntos\n")
    pedido2 = restaurante.crear_pedido("ana@email.com")
    pedido2.agregar_plato(plato5)  # 14€
    pedido2.agregar_plato(plato3)  # 6€
    pedido2.agregar_plato(plato4)  # 2€
    pedido2.propina = 3.00
    pedido2.completar()

    # Total pedido2: 22€ + 3€ = 25€ → 2 puntos
    # Total acumulado: 2 + 2 = 4 puntos
    assert cliente1.puntos == 4, f"❌ Cliente debería tener 4 puntos, tiene {cliente1.puntos}"
    print(f"✅ Segundo pedido completado")
    print(f"   Total gastado por Ana: {cliente1.total_gastado}€")
    print(f"   Puntos totales: {cliente1.puntos}\n")

    # Test 5: Simular muchos puntos y aplicar descuento
    print("=" * 70)
    print("\n💎 TEST 5: Sistema de descuentos por puntos\n")
    # Dar puntos manualmente para probar descuentos
    cliente1.agregar_puntos(96)  # Total: 4 + 96 = 100 puntos

    pedido3 = restaurante.crear_pedido("ana@email.com")
    pedido3.agregar_plato(plato2)  # 12€
    pedido3.agregar_plato(plato1)  # 8.5€
    pedido3.agregar_plato(plato3)  # 6€
    # Subtotal: 26.5€

    descuento = pedido3.aplicar_descuento_puntos(cliente1)

    assert descuento == 15.0, f"❌ Descuento debería ser 15€ (100 puntos), es {descuento}€"
    assert cliente1.puntos == 0, f"❌ Cliente debería tener 0 puntos después del descuento"
    assert pedido3.total == 11.5, f"❌ Total debería ser 11.5€ (26.5 - 15), es {pedido3.total}€"

    print(f"✅ Descuento aplicado: {descuento}€")
    print(f"   Subtotal: {pedido3.subtotal}€")
    print(f"   Total con descuento: {pedido3.total}€")
    print(f"   Puntos restantes: {cliente1.puntos}\n")

    pedido3.completar()

    # Test 6: Cliente con más pedidos
    print("=" * 70)
    print("\n🏆 TEST 6: Cliente más frecuente\n")

    # Luis hace un pedido
    pedido4 = restaurante.crear_pedido("luis@email.com")
    pedido4.agregar_plato(plato2)
    pedido4.completar()

    cliente_top = restaurante.cliente_mas_frecuente()
    assert cliente_top == cliente1, "❌ Ana debería ser la cliente más frecuente (3 pedidos vs 1)"
    print(f"✅ Cliente más frecuente: {cliente_top.nombre}")
    print(f"   Pedidos completados: {len([p for p in cliente_top.pedidos if p.estado == 'completado'])}\n")

    # Test 7: Métodos especiales
    print("=" * 70)
    print("\n🔍 TEST 7: Métodos especiales\n")

    print(f"str(plato1): {plato1}")
    print(f"repr(plato1): {repr(plato1)}")
    print(f"str(cliente1): {cliente1}")
    print(f"str(pedido1): {pedido1}")

    plato_duplicado = Plato("Ensalada César", 10.00, "entrante")
    assert plato1 == plato_duplicado, "❌ Platos con mismo nombre deberían ser iguales"
    print(f"✅ Igualdad de platos por nombre funciona\n")

    # Test 8: Listar por categoría
    print("=" * 70)
    print("\n📋 TEST 8: Listar platos por categoría\n")

    principales = restaurante.listar_platos_por_categoria("principal")
    assert len(principales) == 2, "❌ Debería haber 2 platos principales"
    print(f"✅ Platos principales: {len(principales)}")
    for plato in principales:
        print(f"   - {plato.nombre}: {plato.precio}€")
    print()

    # Test 9: Ingresos totales
    print("=" * 70)
    print("\n💵 TEST 9: Calcular ingresos totales\n")

    ingresos = restaurante.calcular_ingresos_totales()
    # pedido1: 25€, pedido2: 25€, pedido3: 11.5€, pedido4: 12€ = 73.5€
    assert ingresos == 73.5, f"❌ Ingresos deberían ser 73.5€, son {ingresos}€"
    print(f"✅ Ingresos totales: {ingresos}€\n")

    # Test 10: Reporte general
    print("=" * 70)
    print("\n📊 TEST 10: Reporte general\n")
    restaurante.generar_reporte()

    print("\n" + "=" * 70)
    print("\n🎉 ¡TODOS LOS TESTS PASARON! Sistema completo funcionando.\n")
    print("=" * 70)


if __name__ == "__main__":
    # Descomenta cuando termines:
    test_sistema_restaurante()

    # Para probar manualmente:
    # restaurante = Restaurante("Mi Restaurante")
    # plato = Plato("Pizza", 10.0, "principal")
    # restaurante.agregar_plato(plato)
    pass