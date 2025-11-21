from enum import Enum

class EstadoPedido(Enum):
    """
    Clase que representa los estados de un pedido.
    """
    PENDIENTE = "Pendiente"
    CONFIRMADO = "Confirmado"
    ENVIADO = "Enviado"
    ENTREGADO = "Entregado"