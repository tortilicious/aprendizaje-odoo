from datetime import datetime
from typing import TYPE_CHECKING

from config import IVA, FACTOR_CONVERSION_PUNTOS
from models.estado_pedido import EstadoPedido
from models.producto import Producto

if TYPE_CHECKING:
    from models.cliente import Cliente


class Pedido:
    """
    Clase que representa un pedido de un cliente.

    Atributos:
        id: Número de identificación del pedido
        cliente: El cliente que realiza el pedido.
        productos: Diccionario que contiene los productos del pedido y su cantidad.
        estado: Estado actual del pedido.
        fecha_creacion: Registra la hora a la que se crea el pedido
    """
    _id: int = 0

    def __init__(self, cliente: 'Cliente') -> None:
        """
        Crea un nuevo pedido para un cliente.
        Args:
            cliente: objeto Cliente al que pertenece el pedido.
        Raises:
            TypeError: Si el cliente no es un objeto Cliente.
        """

        Pedido._id += 1

        self.id: int = Pedido._id
        self.cliente: 'Cliente' = cliente
        self.productos: dict[Producto, int] = {}  # {producto: cantidad}
        self.estado: EstadoPedido = EstadoPedido.PENDIENTE
        self.fecha_creacion: datetime = datetime.now()

    @property
    def subtotal(self) -> float:
        """
        Calcula el total del pedido sin IVA ni descuentos.
        Returns:
            Suma de (precio × cantidad) de todos los productos.
            Retorna 0 si el pedido está vacío.
        """
        return sum(producto.precio * cantidad for producto, cantidad in self.productos.items())

    @property
    def descuento_aplicado(self) -> float:
        """
        Calcula el precio del pedido una vez aplicado el descuento.
        Returns:
            Precio del pedido con descuento aplicado.
        """
        return self.cliente.descuento * self.subtotal

    @property
    def total(self) -> float:
        """
        Calcula el precio final del pedido con IVA y descuento aplicado.
        Returns:
            Precio total del pedido después de aplicar descuento e IVA.
        """
        return (self.subtotal - self.descuento_aplicado) * IVA

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        """
        Agrega un producto al pedido.
        Args:
            producto: Producto a agregar.
            cantidad: Cantidad del producto a agregar.
        Raises:
            ValueError: Si la cantidad es negativa.
            ValueError: Si la cantidad es mayor al stock.
        Returns:
            None
        """
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser positiva")
        if producto.stock < cantidad:
            raise ValueError("No hay suficiente stock")

        producto.vender(cantidad)
        self.productos[producto] = cantidad

    def cambiar_estado(self, nuevo_estado: EstadoPedido) -> None:
        """
        Actualiza el estado del pedido.
        Args:
            nuevo_estado: Nuevo estado del pedido.
        Returns:
            None
        """
        self.estado = nuevo_estado

    def generar_factura(self) -> str:
        """
        Genera una factura para el pedido.

        Returns:
            String formateado con:
            - ID del pedido
            - Información del cliente
            - Listado de productos con cantidades y precios
            - Subtotal, descuento aplicado, IVA
            - Total final
            - Puntos ganados
        """
        factura = f"""
    ================== FACTURA ==================
    ID Pedido: {self.id}
    Cliente: {self.cliente}
    ==========================================

    """

        # Acumular líneas de productos
        for producto, cantidad in self.productos.items():
            subtotal_producto = producto.precio * cantidad
            linea = f"{producto.nombre}: {cantidad} x ${producto.precio} = ${subtotal_producto}\n"
            factura += linea

        # Añadir totales
        factura += f"""
    ==========================================
    Subtotal: ${self.subtotal:.2f}
    Descuento ({self.cliente.descuento * 100}%): -${self.descuento_aplicado:.2f}
    IVA ({(IVA - 1) * 100}%): ${(self.subtotal - self.descuento_aplicado) * (IVA - 1):.2f}
    Total: ${self.total:.2f}

    Puntos ganados: {int(self.subtotal / FACTOR_CONVERSION_PUNTOS)}
    ==========================================
    """
        return factura
