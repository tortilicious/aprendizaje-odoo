from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from models.producto import Producto

class Tienda:
    """
    Clase que representa una tienda.
    Atributos:
        productos: Lista de productos disponibles.
        clientes: Lista de clientes registrados.
        pedidos: Lista de pedidos realizados.
    """

    def __init__(self):
        self.productos = []
        self.clientes = []
        self.pedidos = []

    # Métodos CRUD Productos

    def crear_producto(self, producto: 'Producto') -> None:
        self.productos.append(producto)

    def buscar_producto_id(self, id_producto: int)-> Optional['Producto']:
        producto = next((producto for producto in self.productos if producto.id == id_producto), None)

    def buscar_producto_nombre(self, nombre_producto: str)-> Optional['Producto']:
        producto = next((producto for producto in self.productos if producto.nombre == nombre_producto), None)

    def actualizar_producto(self, id_producto: int,
                            nombre: str = None,
                            precio:float = None,
                            categoria:str = None) ->  'Producto':

        producto = self.buscar_producto_id(id_producto)
        if not producto:
            raise ValueError("El producto no existe.")

        if nombre is not None: producto.nombre = nombre
        if precio is not None: producto.precio = precio
        if categoria is not None: producto.categoria = categoria
        return producto

    def eliminar_producto(self, id_producto: int) -> None:
        producto = self.buscar_producto_id(id_producto)
        if not producto:
            raise ValueError("El producto no existe.")
        self.productos.remove(producto)




