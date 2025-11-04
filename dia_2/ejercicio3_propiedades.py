"""
EJERCICIO 3: Propiedades con @property

Objetivo: Usar decorador @property para crear getters/setters pythónicos

CONCEPTOS:
- @property: Convierte un método en un atributo de solo lectura
- @atributo.setter: Define el setter
- Validación en setters
- Propiedades calculadas (solo getter)

COMPARACIÓN CON JAVA:
Java:                                   Python:
private double precio;                  def __init__(self):
                                            self._precio = 0
public double getPrecio() {
    return precio;                      @property
}                                       def precio(self):
                                            return self._precio
public void setPrecio(double p) {
    if (p < 0)                          @precio.setter
        throw ...;                      def precio(self, valor):
    this.precio = p;                        if valor < 0:
}                                               raise ValueError(...)
                                            self._precio = valor

// USO Java:                           # USO Python:
producto.getPrecio()                   producto.precio      # getter
producto.setPrecio(100)                producto.precio = 100 # setter

VENTAJA: En Python se accede como atributo pero ejecuta código de validación.
"""


# TODO: Crear clase CuentaBancaria con:
# - Constructor: titular (str), saldo_inicial (float, default=0)
# - Propiedad 'saldo' con:
#   * getter que retorne el saldo
#   * setter que valide que el saldo nunca sea negativo
# - Método depositar(cantidad) que aumente el saldo
# - Método retirar(cantidad) que:
#   * Reduzca el saldo si hay fondos suficientes
#   * Retorne True si se pudo retirar, False si no
# - Propiedad 'esta_en_numeros_rojos' (solo getter):
#   * Retorna True si saldo < 0, False si no

class CuentaBancaria:
    """
    Representa una cuenta bancaria simple.

    Atributos:
        titular (str): Nombre del titular
        _saldo (float): Saldo actual (privado)
    """

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    # Getter
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self._saldo = valor
        else:
            raise ValueError("El saldo no puede ser negativo")

    @property
    def esta_en_numeros_rojos(self):
        return self._saldo < 0

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self, cantidad):
        if self._saldo - cantidad >= 0:
            self._saldo -= cantidad
            return True
        return False


# ============================================================================
# TESTS - No modificar
# ============================================================================

def test_cuenta_bancaria():
    """Tests automáticos para validar tu implementación"""
    print("🧪 Ejecutando tests del Ejercicio 3...\n")

    # Test 1: Creación y getter de saldo
    print("Test 1: Creación y propiedad saldo (getter)")
    cuenta = CuentaBancaria("Juan López", 1000.0)
    assert cuenta.titular == "Juan López"
    # Acceso como atributo (no como método)
    assert cuenta.saldo == 1000.0, "❌ El getter de saldo no funciona"
    print(f"✅ Cuenta creada: Titular={cuenta.titular}, Saldo={cuenta.saldo}€\n")

    # Test 2: Depositar
    print("Test 2: Método depositar()")
    cuenta.depositar(500)
    assert cuenta.saldo == 1500.0, "❌ depositar() no actualiza el saldo"
    print(f"✅ Depósito exitoso. Saldo actual: {cuenta.saldo}€\n")

    # Test 3: Retirar (exitoso)
    print("Test 3: Método retirar() exitoso")
    resultado = cuenta.retirar(200)
    assert resultado == True, "❌ retirar() debería retornar True"
    assert cuenta.saldo == 1300.0, "❌ retirar() no actualiza el saldo"
    print(f"✅ Retiro exitoso. Saldo actual: {cuenta.saldo}€\n")

    # Test 4: Retirar (fallido por fondos insuficientes)
    print("Test 4: Retirar sin fondos suficientes")
    resultado = cuenta.retirar(2000)
    assert resultado == False, "❌ retirar() debería retornar False"
    assert cuenta.saldo == 1300.0, "❌ El saldo NO debería cambiar"
    print(f"✅ Retiro rechazado. Saldo se mantiene: {cuenta.saldo}€\n")

    # Test 5: Setter de saldo con validación
    print("Test 5: Setter de saldo con validación")
    try:
        cuenta.saldo = -100  # Esto debería lanzar excepción
        assert False, "❌ El setter debería validar saldo negativo"
    except ValueError:
        print("✅ Setter valida correctamente (rechaza saldo negativo)\n")

    # Test 6: Setter de saldo válido
    print("Test 6: Setter de saldo válido")
    cuenta.saldo = 2000
    assert cuenta.saldo == 2000, "❌ El setter no asigna correctamente"
    print(f"✅ Saldo actualizado correctamente: {cuenta.saldo}€\n")

    # Test 7: Propiedad calculada esta_en_numeros_rojos
    print("Test 7: Propiedad calculada esta_en_numeros_rojos")
    assert cuenta.esta_en_numeros_rojos == False, "❌ No debería estar en rojo (saldo=2000)"

    # Forzar saldo negativo para test
    cuenta._saldo = -50  # Acceso directo (no recomendado en código real)
    assert cuenta.esta_en_numeros_rojos == True, "❌ Debería estar en rojo (saldo=-50)"
    print("✅ Propiedad calculada funciona correctamente\n")

    print("🎉 ¡Todos los tests pasaron! Ejercicio 3 completado.\n")


if __name__ == "__main__":
    # Descomenta cuando termines:
    test_cuenta_bancaria()

    # Para probar manualmente:
    # cuenta = CuentaBancaria("Ana", 500)
    # print(f"Saldo inicial: {cuenta.saldo}€")
    # cuenta.depositar(200)
    # print(f"Después de depósito: {cuenta.saldo}€")
    # cuenta.retirar(100)
    # print(f"Después de retiro: {cuenta.saldo}€")
    pass
