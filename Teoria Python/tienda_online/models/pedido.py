from datetime import datetime

from models.cliente import Cliente
from models.estado_pedido import EstadoPedido
from models.producto import Producto


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
    IVA: float = 1.21

    def __init__(self, cliente: Cliente) -> None:
        """
        Crea un nuevo pedido para un cliente.
        Args:
            cliente: objeto Cliente al que pertenece el pedido.
        Raises:
            TypeError: Si el cliente no es un objeto Cliente.
        """
        if not isinstance(cliente, Cliente):
            raise TypeError("cliente debe ser instancia de Cliente")

        Pedido._id += 1

        self.id: int = Pedido._id
        self.cliente: Cliente = cliente
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
        return (self.subtotal - self.descuento_aplicado) * self.IVA
