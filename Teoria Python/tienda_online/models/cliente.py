from models.nivel_cliente import NivelCliente
from models.pedido import Pedido
from config import FACTOR_CONVERSION_PUNTOS


class Cliente:
    """
    Clase que representa un cliente.

    Atributos:
        id: Número de identificación del cliente.
        nombre: Nombre del cliente.
        email: Correo del cliente. Debe ser único.
        pedidos: Lista de pedidos del cliente.
    """
    _id: int = 0

    def __init__(self, nombre: str, email: str):
        """
        Crea un nuevo cliente.
        Args:
            nombre: Nombre del cliente.
            email: Email del cliente.
        Raises:
            ValueError: Si el 'nombre' o el 'email' están vacíos.
        """
        if not nombre or not email:
            raise ValueError("Los campos 'nombre' y 'email' no pueden estar vacíos")

        Cliente._id += 1

        self.id: int = Cliente._id
        self.nombre: str = nombre
        self.email: str = email
        self.pedidos: list[Pedido] = []

    def __repr__(self):
        return f"""
        Información del cliente:
            Puntos: {self.puntos}
            Nivel cliente: {self.nivel_cliente}
            
        """

    @property
    def nivel_cliente(self) -> NivelCliente:
        """
        Calcula nivel de cliente en función de los puntos acumulados.
        Returns:
            Categoría de NivelCliente correspondiente.
        """
        if self.puntos < 49:
            return NivelCliente.BRONCE
        elif self.puntos < 150:
            return NivelCliente.PLATA
        else:
            return NivelCliente.ORO

    @property
    def descuento(self) -> float:
        """
        Calcula el descuento del cliente asociado a su nivel de cliente.
        Returns:
            El porcentaje de descuento del cliente.
        """
        if self.nivel_cliente == NivelCliente.PLATA:
            return 0.05
        elif self.nivel_cliente == NivelCliente.ORO:
            return 0.10
        else:
            return 0.00

    @property
    def puntos(self) -> int:
        """
        Calcula los puntos acumulados por todos los pedidos del cliente.
        Returns:
            Puntos acumulados.
        """
        return int(sum(pedido.total for pedido in self.pedidos) / FACTOR_CONVERSION_PUNTOS)

    def agregar_pedido(self, pedido: Pedido) -> None:
        if len(pedido.productos) == 0:
            raise ValueError("No se puede agregar pedidos sin productos")
        self.pedidos.append(pedido)
