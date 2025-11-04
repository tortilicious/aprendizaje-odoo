"""
EJERCICIO 1: Clase Producto (Básico)

Objetivo: Crear tu primera clase en Python con constructor y métodos.

CONCEPTOS:
- Definición de clase
- Constructor __init__
- Atributos de instancia
- Métodos simples
- self (equivalente a this en Java)

COMPARACIÓN CON JAVA:
Java:                           Python:
public class Producto {         class Producto:
    private String nombre;          def __init__(self, nombre, precio):
    private double precio;              self.nombre = nombre
                                        self.precio = precio
    public Producto(...) {
        this.nombre = nombre;
    }
}
"""


# TODO: Crear la clase Producto con:
# - Constructor que reciba: nombre (str), precio (float), stock (int)
# - Método mostrar_info() que retorne un string con toda la información
# - Método esta_disponible() que retorne True si stock > 0
# - Método vender(cantidad) que:
#   * Reduzca el stock si hay suficiente
#   * Retorne True si se pudo vender, False si no hay stock

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"

    def esta_disponible(self):
        return self.stock > 0

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False


def test_producto():
    """Tests automáticos para validar tu implementación"""
    print("🧪 Ejecutando tests del Ejercicio 1...\n")

    # Test 1: Creación básica
    print("Test 1: Creación de producto")
    laptop = Producto("Laptop", 1200.50, 5)
    assert laptop.nombre == "Laptop", "❌ El nombre no se asignó correctamente"
    assert laptop.precio == 1200.50, "❌ El precio no se asignó correctamente"
    assert laptop.stock == 5, "❌ El stock no se asignó correctamente"
    print("✅ Producto creado correctamente\n")

    # Test 2: Método mostrar_info()
    print("Test 2: Método mostrar_info()")
    info = laptop.mostrar_info()
    assert isinstance(info, str), "❌ mostrar_info() debe retornar un string"
    assert "Laptop" in info, "❌ La info debe contener el nombre"
    assert "1200.5" in info or "1200.50" in info, "❌ La info debe contener el precio"
    print(f"✅ Info: {info}\n")

    # Test 3: Método esta_disponible()
    print("Test 3: Método esta_disponible()")
    assert laptop.esta_disponible() == True, "❌ Debería estar disponible (stock=5)"

    producto_sin_stock = Producto("Mouse", 25.0, 0)
    assert producto_sin_stock.esta_disponible() == False, "❌ No debería estar disponible (stock=0)"
    print("✅ Disponibilidad correcta\n")

    # Test 4: Método vender()
    print("Test 4: Método vender()")
    resultado = laptop.vender(2)
    assert resultado == True, "❌ La venta debería ser exitosa"
    assert laptop.stock == 3, "❌ El stock debería reducirse a 3"
    print("✅ Venta exitosa, stock actualizado\n")

    # Test 5: Venta sin stock suficiente
    print("Test 5: Venta sin stock suficiente")
    resultado = laptop.vender(10)
    assert resultado == False, "❌ La venta debería fallar (stock insuficiente)"
    assert laptop.stock == 3, "❌ El stock NO debería cambiar si la venta falla"
    print("✅ Venta rechazada correctamente\n")

    print("🎉 ¡Todos los tests pasaron! Ejercicio 1 completado.\n")


if __name__ == "__main__":
    # Descomenta cuando termines la implementación:
    test_producto()

    # Para probar manualmente:
    # p = Producto("Teclado", 45.99, 10)
    # print(p.mostrar_info())
    # print(p.esta_disponible())
    # p.vender(3)
    # print(p.mostrar_info())
    pass