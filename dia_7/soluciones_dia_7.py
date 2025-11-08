# ✅ SOLUCIONES COMENTADAS - DÍA 7: LAMBDA, TYPE HINTS, MÓDULOS Y PROYECTO FINAL
# ==================================================================================

"""
IMPORTANTE: 
- Estas son SOLUCIONES COMENTADAS
- Pueden haber otras formas correctas
- Lo importante es ENTENDER cada concepto
- Este es el último día antes de Odoo
"""

# =============================================================================
# EJERCICIO 1: Filtrar Productos por Precio
# =============================================================================

print("--- Ejercicio 1: Filtrar con filter() y lambda ---\n")

productos = [
    {'nombre': 'Laptop', 'precio': 1200},
    {'nombre': 'Mouse', 'precio': 20},
    {'nombre': 'Monitor', 'precio': 300},
    {'nombre': 'Teclado', 'precio': 80},
    {'nombre': 'Cable', 'precio': 5},
]

# 1. Productos menores a 100€
menores_100 = list(filter(lambda p: p['precio'] < 100, productos))
print("1. Productos menores a 100€:")
for p in menores_100:
    print(f"   {p['nombre']}: {p['precio']}€")

# 2. Productos mayores a 50€
mayores_50 = list(filter(lambda p: p['precio'] > 50, productos))
print("\n2. Productos mayores a 50€:")
for p in mayores_50:
    print(f"   {p['nombre']}: {p['precio']}€")

# 3. Filtrar Y ordenar por precio
filtrados_ordenados = sorted(
    filter(lambda p: p['precio'] < 500, productos),
    key=lambda p: p['precio']
)
print("\n3. Menores a 500€ ordenados por precio:")
for p in filtrados_ordenados:
    print(f"   {p['nombre']}: {p['precio']}€")


# =============================================================================
# EJERCICIO 2: Transformar Datos con map() y Lambda
# =============================================================================

print("\n--- Ejercicio 2: Transformar con map() y lambda ---\n")

precios_euros = [10, 20, 50, 100]

# 1. Convertir a dólares (multiplicar por 1.10)
dolares = list(map(lambda p: p * 1.10, precios_euros))
print(f"1. En dólares: {dolares}")

# 2. Aplicar IVA 21%
con_iva = list(map(lambda p: p * 1.21, precios_euros))
print(f"2. Con IVA 21%: {con_iva}")

# 3. Redondear a 2 decimales
redondeados = list(map(lambda p: round(p * 1.21, 2), precios_euros))
print(f"3. Redondeados: {redondeados}")

# BONUS: Todo en una línea
pipeline = list(map(
    lambda p: round(p * 1.21, 2),  # IVA y redondear
    precios_euros
))
print(f"\nBONUS (todo en una línea): {pipeline}")


# =============================================================================
# EJERCICIO 3: Ordenar Datos Complejos
# =============================================================================

print("\n--- Ejercicio 3: sorted() con lambda ---\n")

pedidos = [
    {'cliente': 'Ana', 'total': 150, 'fecha': '2025-01-05'},
    {'cliente': 'Luis', 'total': 75, 'fecha': '2025-01-03'},
    {'cliente': 'María', 'total': 150, 'fecha': '2025-01-04'},
]

# 1. Ordenar por total (menor a mayor)
por_total = sorted(pedidos, key=lambda p: p['total'])
print("1. Por total (menor a mayor):")
for p in por_total:
    print(f"   {p['cliente']}: {p['total']}€")

# 2. Ordenar por total (mayor a menor)
por_total_desc = sorted(pedidos, key=lambda p: p['total'], reverse=True)
print("\n2. Por total (mayor a menor):")
for p in por_total_desc:
    print(f"   {p['cliente']}: {p['total']}€")

# 3. Ordenar por cliente (alfabético)
por_cliente = sorted(pedidos, key=lambda p: p['cliente'])
print("\n3. Por cliente (alfabético):")
for p in por_cliente:
    print(f"   {p['cliente']}: {p['total']}€")

# 4. Por cliente y total (múltiples criterios)
por_cliente_total = sorted(pedidos, key=lambda p: (p['cliente'], p['total']))
print("\n4. Por cliente, luego por total:")
for p in por_cliente_total:
    print(f"   {p['cliente']}: {p['total']}€")


# =============================================================================
# EJERCICIO 4: Pipeline map + filter + sorted
# =============================================================================

print("\n--- Ejercicio 4: Pipeline completo ---\n")

datos = [
    {'id': 1, 'valor': -50},
    {'id': 2, 'valor': 100},
    {'id': 3, 'valor': -20},
    {'id': 4, 'valor': 200},
    {'id': 5, 'valor': 75},
]

# Pipeline: filtrar → transformar → ordenar
resultado = sorted(
    map(
        lambda d: d['valor'] * 2,
        filter(
            lambda d: d['valor'] > 0,  # Solo positivos
            datos
        )
    ),
    reverse=True  # Orden descendente
)

print(f"Resultado final: {resultado}")
# [400, 200, 150]

# Alternativa con list comprehension (más legible):
resultado_alt = sorted(
    [d['valor'] * 2 for d in datos if d['valor'] > 0],
    reverse=True
)
print(f"Alternativa (comprehension): {resultado_alt}")


# =============================================================================
# EJERCICIO 5: Type Hints - Añadir a Funciones
# =============================================================================

print("\n--- Ejercicio 5: Type Hints ---\n")

from typing import List, Dict, Optional, Tuple

def filtrar_pares(numeros: List[int]) -> List[int]:
    """Filtra solo números pares de una lista"""
    return [n for n in numeros if n % 2 == 0]


def obtener_datos_usuario(usuarios: Dict[int, Dict], id: int) -> Optional[Dict]:
    """Obtiene datos de un usuario por ID, o None si no existe"""
    return usuarios.get(id)


def procesar_pedido(cliente: str, productos: List[Dict], cantidad: int) -> Dict:
    """Procesa un pedido y retorna resumen con total"""
    total = sum([p['precio'] for p in productos]) * cantidad
    return {'cliente': cliente, 'total': total}


def buscar_minimo(valores: List[int]) -> Optional[int]:
    """Encuentra el mínimo de una lista, retorna None si está vacía"""
    if not valores:
        return None
    return min(valores)


# Pruebas
print("1. Filtrar pares de [1, 2, 3, 4, 5]:")
print(filtrar_pares([1, 2, 3, 4, 5]))

usuarios = {1: {'nombre': 'Ana'}, 2: {'nombre': 'Luis'}}
print("\n2. Obtener usuario 1:")
print(obtener_datos_usuario(usuarios, 1))

productos_ej = [{'precio': 10}, {'precio': 20}]
print("\n3. Procesar pedido:")
print(procesar_pedido("Juan", productos_ej, 2))

print("\n4. Mínimo de [5, 2, 8, 1]:")
print(buscar_minimo([5, 2, 8, 1]))


# =============================================================================
# EJERCICIO 6: Type Hints en Proyecto Odoo-like
# =============================================================================

print("\n--- Ejercicio 6: Type Hints Avanzados ---\n")

from typing import Tuple

def obtener_producto_por_id(productos: List[Dict], id: int) -> Optional[Dict]:
    """Obtiene un producto por ID, retorna None si no existe"""
    for prod in productos:
        if prod['id'] == id:
            return prod
    return None


def calcular_total_carrito(items: List[Dict[str, float]]) -> float:
    """Calcula el total de un carrito de compras"""
    return sum(item['precio'] * item.get('cantidad', 1) for item in items)


def aplicar_descuento(total: float, porcentaje: float) -> Tuple[float, float, float]:
    """
    Aplica descuento y retorna (original, descuento, final)
    """
    descuento_aplicado = total * (porcentaje / 100)
    total_final = total - descuento_aplicado
    return (total, descuento_aplicado, total_final)


def validar_email(email: str) -> bool:
    """Valida un email (validación simple)"""
    return '@' in email and '.' in email


def agrupar_por_categoria(productos: List[Dict]) -> Dict[str, List[Dict]]:
    """Agrupa productos por categoría"""
    resultado: Dict[str, List[Dict]] = {}
    for prod in productos:
        cat = prod['categoria']
        if cat not in resultado:
            resultado[cat] = []
        resultado[cat].append(prod)
    return resultado


# Pruebas
print("1. Obtener producto:")
prods = [{'id': 1, 'nombre': 'Laptop'}, {'id': 2, 'nombre': 'Mouse'}]
print(obtener_producto_por_id(prods, 1))

print("\n2. Total carrito:")
carrito = [{'precio': 10, 'cantidad': 2}, {'precio': 20, 'cantidad': 1}]
print(f"Total: {calcular_total_carrito(carrito)}€")

print("\n3. Aplicar 10% descuento a 100€:")
original, desc, final = aplicar_descuento(100, 10)
print(f"  Original: {original}€, Descuento: {desc}€, Final: {final}€")

print("\n4. Validar email:")
print(f"  ana@email.com: {validar_email('ana@email.com')}")
print(f"  anamail.com: {validar_email('anamail.com')}")


# =============================================================================
# EJERCICIO 7: Organizar Código en Módulos
# =============================================================================

print("\n--- Ejercicio 7: Estructura de Módulos ---\n")

print("""
Estructura creada:

tienda/
├── main.py              # Ejecutable principal
├── decoradores.py       # Decoradores personalizados
├── utils.py            # Funciones de utilidad
└── models/
    ├── __init__.py
    ├── producto.py
    └── cliente.py

Ejemplo de imports en main.py:

from decoradores import con_logging
from utils import agrupar_por
from models import Producto, Cliente

Los archivos estarían en el repositorio de GitHub.
""")


# =============================================================================
# 🎯 PROYECTO FINAL: SISTEMA DE TIENDA ONLINE (VERSIÓN SIMPLIFICADA)
# =============================================================================

print("\n" + "="*70)
print("🎯 PROYECTO FINAL: SISTEMA DE TIENDA ONLINE")
print("="*70 + "\n")

from functools import wraps
from collections import defaultdict
from datetime import datetime

# -------- DECORADORES --------

def con_logging(func):
    """Decorador para registrar llamadas a funciones"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Llamada: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"✅ Completado: {func.__name__}")
        return resultado
    return wrapper


# -------- MODELOS --------

class Producto:
    """Modelo de Producto"""
    
    IVA = 0.21
    
    def __init__(self, id: int, nombre: str, precio: float, stock: int, categoria: str):
        self.id = id
        self.nombre = nombre
        self._precio = precio
        self._stock = stock
        self.categoria = categoria
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("❌ Precio no puede ser negativo")
        self._precio = valor
    
    @property
    def precio_con_iva(self) -> float:
        """Calcula precio con IVA"""
        return self._precio * (1 + self.IVA)
    
    @property
    def stock(self) -> int:
        return self._stock
    
    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("❌ Stock no puede ser negativo")
        self._stock = valor
    
    @property
    def stock_bajo(self) -> bool:
        """Verifica si stock está bajo (< 5)"""
        return self._stock < 5
    
    def vender(self, cantidad: int) -> bool:
        """Vende un producto (reduce stock)"""
        if cantidad > self._stock:
            raise ValueError(f"❌ Stock insuficiente. Disponible: {self._stock}")
        self._stock -= cantidad
        return True
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self._precio}€ ({self._stock} ud.)"


class Cliente:
    """Modelo de Cliente con puntos de fidelidad"""
    
    NIVELES_DESCUENTO = {
        'Bronce': 0.0,    # 0-50 puntos
        'Plata': 0.05,    # 50-150 puntos - 5% descuento
        'Oro': 0.10,      # 150+ puntos - 10% descuento
    }
    
    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self._puntos = 0
        self._pedidos: List = []
    
    @property
    def puntos(self) -> int:
        return self._puntos
    
    @property
    def nivel(self) -> str:
        """Determina nivel según puntos"""
        if self._puntos < 50:
            return 'Bronce'
        elif self._puntos < 150:
            return 'Plata'
        else:
            return 'Oro'
    
    @property
    def descuento(self) -> float:
        """Retorna descuento según nivel"""
        return self.NIVELES_DESCUENTO[self.nivel]
    
    def agregar_puntos(self, cantidad: int) -> None:
        """Añade puntos de fidelidad"""
        if cantidad < 0:
            raise ValueError("❌ Puntos no pueden ser negativos")
        self._puntos += cantidad
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.email}) - {self._puntos} pts ({self.nivel})"


class Pedido:
    """Modelo de Pedido"""
    
    ESTADOS = ['Pendiente', 'Confirmado', 'Enviado', 'Entregado']
    
    def __init__(self, id: int, cliente: Cliente):
        self.id = id
        self.cliente = cliente
        self.fecha = datetime.now()
        self.productos: List[Tuple[Producto, int]] = []  # (producto, cantidad)
        self.estado = 'Pendiente'
        self.descuento_manual = 0.0
    
    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        """Añade producto al pedido"""
        if cantidad <= 0:
            raise ValueError("❌ Cantidad debe ser > 0")
        self.productos.append((producto, cantidad))
    
    @property
    def subtotal(self) -> float:
        """Subtotal sin descuentos"""
        return sum(prod.precio * cant for prod, cant in self.productos)
    
    @property
    def descuento_fidelidad(self) -> float:
        """Descuento por nivel de cliente"""
        return self.subtotal * self.cliente.descuento
    
    @property
    def descuento_total(self) -> float:
        """Descuento total"""
        return self.descuento_fidelidad + self.descuento_manual
    
    @property
    def total(self) -> float:
        """Total a pagar"""
        return self.subtotal - self.descuento_total
    
    @con_logging
    def confirmar(self) -> None:
        """Confirma pedido, vende productos y genera puntos"""
        if self.estado != 'Pendiente':
            raise ValueError("❌ Solo puedes confirmar pedidos Pendientes")
        
        # Vender productos
        for producto, cantidad in self.productos:
            producto.vender(cantidad)
        
        # Cambiar estado
        self.estado = 'Confirmado'
        
        # Generar puntos (1 punto cada 10€)
        puntos_ganados = int(self.total / 10)
        self.cliente.agregar_puntos(puntos_ganados)
    
    def generar_factura(self) -> str:
        """Genera factura de texto"""
        factura = [
            "\n" + "="*50,
            "FACTURA - TIENDA ONLINE",
            "="*50,
            f"Pedido: #{self.id}",
            f"Cliente: {self.cliente.nombre}",
            f"Estado: {self.estado}",
            "-"*50,
            "PRODUCTOS:",
        ]
        
        for producto, cantidad in self.productos:
            subtotal = producto.precio * cantidad
            factura.append(f"  {producto.nombre} x{cantidad} ... {subtotal}€")
        
        factura.extend([
            "-"*50,
            f"Subtotal: {self.subtotal:.2f}€",
            f"Descuento: -{self.descuento_total:.2f}€",
            f"TOTAL: {self.total:.2f}€",
            f"Puntos ganados: {int(self.total / 10)}",
            "="*50 + "\n",
        ])
        
        return "\n".join(factura)
    
    def __str__(self) -> str:
        return f"Pedido #{self.id} - {self.cliente.nombre} - {self.total:.2f}€"


class TiendaOnline:
    """Gestor principal de la tienda"""
    
    def __init__(self):
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []
        self.pedidos: List[Pedido] = []
        self.id_producto = 1
        self.id_cliente = 1
        self.id_pedido = 1
    
    def agregar_producto(self, nombre: str, precio: float, stock: int, categoria: str) -> Producto:
        """Crea un nuevo producto"""
        producto = Producto(self.id_producto, nombre, precio, stock, categoria)
        self.productos.append(producto)
        self.id_producto += 1
        return producto
    
    def registrar_cliente(self, nombre: str, email: str) -> Cliente:
        """Registra un nuevo cliente"""
        if any(c.email == email for c in self.clientes):
            raise ValueError(f"❌ Email {email} ya registrado")
        
        cliente = Cliente(self.id_cliente, nombre, email)
        self.clientes.append(cliente)
        self.id_cliente += 1
        return cliente
    
    def crear_pedido(self, email_cliente: str) -> Pedido:
        """Crea un nuevo pedido"""
        cliente = next((c for c in self.clientes if c.email == email_cliente), None)
        if not cliente:
            raise ValueError(f"❌ Cliente con email {email_cliente} no encontrado")
        
        pedido = Pedido(self.id_pedido, cliente)
        self.pedidos.append(pedido)
        self.id_pedido += 1
        return pedido
    
    def filtrar_por_precio(self, min_precio: float, max_precio: float) -> List[Producto]:
        """Filtra productos por rango de precio"""
        return [p for p in self.productos if min_precio <= p.precio <= max_precio]
    
    def productos_en_oferta(self) -> List[Producto]:
        """Retorna productos con stock bajo"""
        return [p for p in self.productos if p.stock_bajo]
    
    def clientes_por_nivel(self) -> Dict[str, List[Cliente]]:
        """Agrupa clientes por nivel"""
        agrupado: Dict[str, List[Cliente]] = defaultdict(list)
        for cliente in self.clientes:
            agrupado[cliente.nivel].append(cliente)
        return dict(agrupado)
    
    def generador_productos(self):
        """Generador: procesa productos uno a uno"""
        for producto in self.productos:
            yield producto
    
    def mostrar_catalogo(self) -> None:
        """Muestra catálogo organizado por categoría"""
        print("\n" + "="*60)
        print("📦 CATÁLOGO DE PRODUCTOS")
        print("="*60)
        
        # Agrupar por categoría
        por_categoria: Dict[str, List[Producto]] = defaultdict(list)
        for prod in self.productos:
            por_categoria[prod.categoria].append(prod)
        
        # Mostrar
        for categoria in sorted(por_categoria.keys()):
            print(f"\n🏷️  {categoria.upper()}")
            print("-" * 60)
            for prod in sorted(por_categoria[categoria], key=lambda p: p.precio):
                disponible = "✅" if prod.stock > 0 else "❌"
                print(f"  {disponible} {prod.nombre}: {prod.precio}€ ({prod.stock} ud.)")
    
    def mostrar_clientes(self) -> None:
        """Muestra clientes ordenados por puntos"""
        print("\n" + "="*60)
        print("👥 CLIENTES")
        print("="*60)
        
        for cliente in sorted(self.clientes, key=lambda c: c.puntos, reverse=True):
            print(f"  {cliente}")
    
    def reporte_ventas(self) -> None:
        """Genera reporte de ventas"""
        print("\n" + "="*60)
        print("💰 REPORTE DE VENTAS")
        print("="*60)
        
        confirmados = [p for p in self.pedidos if p.estado == 'Confirmado']
        total_ventas = sum(p.total for p in confirmados)
        
        print(f"  Total de pedidos: {len(self.pedidos)}")
        print(f"  Pedidos confirmados: {len(confirmados)}")
        print(f"  Total de ventas: {total_ventas:.2f}€")
        print(f"  Clientes: {len(self.clientes)}")
        print(f"  Ticket promedio: {total_ventas / len(confirmados):.2f}€" if confirmados else "")


# -------- DEMOSTRACIÓN --------

def demo():
    """Demostración completa del sistema"""
    
    tienda = TiendaOnline()
    
    # 1. Agregar productos
    print("\n📦 Agregando productos...")
    laptop = tienda.agregar_producto("Laptop", 1200, 3, "Electrónica")
    mouse = tienda.agregar_producto("Mouse", 20, 50, "Accesorios")
    monitor = tienda.agregar_producto("Monitor", 300, 2, "Electrónica")
    teclado = tienda.agregar_producto("Teclado", 80, 0, "Accesorios")
    
    # 2. Registrar clientes
    print("\n👥 Registrando clientes...")
    ana = tienda.registrar_cliente("Ana López", "ana@email.com")
    luis = tienda.registrar_cliente("Luis García", "luis@email.com")
    maria = tienda.registrar_cliente("María Pérez", "maria@email.com")
    
    # 3. Mostrar catálogo
    tienda.mostrar_catalogo()
    
    # 4. Cliente Ana hace compra
    print("\n📝 Ana realiza compra...")
    pedido1 = tienda.crear_pedido("ana@email.com")
    pedido1.agregar_producto(laptop, 1)
    pedido1.agregar_producto(mouse, 2)
    print(f"Subtotal: {pedido1.subtotal}€")
    print(f"Descuento: -{pedido1.descuento_total}€")
    print(f"Total: {pedido1.total}€")
    
    # 5. Confirmar pedido
    pedido1.confirmar()
    print(pedido1.generar_factura())
    
    # 6. Más compras para Ana (acumule puntos)
    print("\n📝 Ana hace otra compra...")
    pedido2 = tienda.crear_pedido("ana@email.com")
    pedido2.agregar_producto(monitor, 1)
    pedido2.confirmar()
    
    print(f"Ana ahora tiene: {ana.puntos} puntos ({ana.nivel})")
    
    # 7. Luis hace compra (con descuento si sube de nivel)
    print("\n📝 Luis realiza compra...")
    pedido3 = tienda.crear_pedido("luis@email.com")
    pedido3.agregar_producto(teclado, 1)
    pedido3.confirmar()
    
    # 8. Mostrar clientes
    tienda.mostrar_clientes()
    
    # 9. Filtrar productos
    print("\n🔍 Productos entre 50€ y 400€:")
    filtrados = tienda.filtrar_por_precio(50, 400)
    for p in filtrados:
        print(f"  - {p.nombre}: {p.precio}€")
    
    # 10. Reporte final
    tienda.reporte_ventas()


# Ejecutar demostración
if __name__ == "__main__":
    demo()


# =============================================================================
# NOTAS FINALES
# =============================================================================

print("\n" + "="*70)
print("✅ PROYECTO FINAL COMPLETADO")
print("="*70)

print("""
📊 LO QUE HAS IMPLEMENTADO:

✅ DECORADORES:
   - @con_logging para registrar operaciones

✅ GENERADORES:
   - generador_productos() para procesar datos

✅ CONTEXT MANAGERS:
   - Podrían usarse para transacciones de BD

✅ DICCIONARIOS AVANZADOS:
   - Agrupación por categoría
   - Filtros complejos
   - Merge de configuraciones

✅ LAMBDA:
   - sorted() con key=lambda
   - filter() con lambda

✅ TYPE HINTS:
   - Todas las funciones con type hints
   - Código documentado

✅ MÓDULOS:
   - Código organizado en clases
   - Fácil de expandir

🎯 PRÓXIMOS PASOS - SEMANA 2: ODOO

Con esto ya dominas:
✅ Decoradores (@api.depends, @api.onchange)
✅ Diccionarios (vals, context, domain)
✅ Type hints (código profesional)
✅ Módulos (estructura de Odoo)

¡ESTÁS LISTO PARA LAS PRÁCTICAS! 🚀
""")

print("✅ TODAS LAS SOLUCIONES DEL DÍA 7 COMPLETADAS")