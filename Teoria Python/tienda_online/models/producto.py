from datetime import datetime
from config import IVA

class Producto:
    """
    Clase que representa un producto.

    Atributos:
        id: Número de identificación del producto.
        nombre: Nombre del producto.
        precio: Precio del producto.
        categoria: Categoría a la que pertenece el producto.
        stock: Cantidad de productos disponibles.
        fecha_creacion: Fecha en la que fue creado el producto.
    """
    _id: int = 0

    def __init__(self, nombre: str, precio: float, categoria: str):
        """
        Crea un nuevo producto.
        Args:
            nombre: Nombre del producto.
            precio: Precio del producto.
            categoria: Categoría a la que pertenece el producto.
        Raises:
            ValueError: Si el nombre o la categoría están vacíos.
            ValueError: Si el precio es negativo.
        """

        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if not nombre or not categoria:
            raise ValueError("Nombre y categoría no pueden estar vacíos")

        Producto._id += 1

        self.id: int = Producto._id
        self._nombre: str = nombre
        self._precio: float = precio
        self._categoria: str = categoria
        self.stock: int = 0
        self.fecha_creacion: datetime = datetime.now()

    def __repr__(self):
        return f"""
        Producto: {self.nombre}
            Precio: {self.precio}
            Categoria: {self.categoria}
            Stock: {self.stock}
        """

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El campo de nombre no puede estar vacío")
        self._nombre = nuevo_nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        if not nueva_categoria:
            raise ValueError("El campo de categoría no puede estar vacio")
        self._categoria = nueva_categoria


    @property
    def precio_con_iva(self) -> float:
        """
        Calcula el precio del producto con IVA.
        Returns: precio base del producto + IVA
        """
        return self.precio * IVA

    @property
    def stock_bajo(self) -> bool:
        """
        Comprueba si el stock del producto es bajo
        Returns: True si el stock es menor a 5
        """
        return self.stock < 5

    def vender(self, cantidad: int) -> None:
        """
        Descuenta la cantidad de stock del producto.
        Args:
            cantidad: Cantidad de productos a vender.
        Returns:
            None
        Raises:
            ValueError: Si la cantidad de productos a vender es mayor al stock.
            ValueError: Si la cantidad de productos a vender es negativa.
        """
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock")
        if cantidad <= 0:
            raise ValueError("No se puede vender una cantidad negativa")
        self.stock -= cantidad

    def reponer_stock(self, cantidad: int) -> None:
        """
        Aumenta la cantidad de stock del producto.
        Args:
            cantidad: Cantidad de productos a reponer.
        Returns:
            None
        Raises:
            ValueError: Si la cantidad de productos a reponer es negativa.
        """
        if cantidad <= 0:
            raise ValueError("No se puede reponer stock negativo")
        self.stock += cantidad
