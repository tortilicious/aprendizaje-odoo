class Cliente:
    def __init__(self, nombre, email, vip):
        self.nombre = nombre
        self.email = email
        self.vip = vip

    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email}) {" VIP" if self.vip else ""}"

    def __repr__(self):
        return f"Cliente(nombre='{self.nombre}', email='{self.email}', vip={self.vip})"

    def __eq__(self, otro_cliente):
        return self.email == otro_cliente.email


# ============================================================================
# TESTS - No modificar
# ============================================================================

def test_cliente():
    """Tests automáticos para validar tu implementación"""
    print("🧪 Ejecutando tests del Ejercicio 2...\n")

    # Test 1: Creación básica
    print("Test 1: Creación de cliente")
    c1 = Cliente("Ana García", "ana@email.com", True)
    assert c1.nombre == "Ana García"
    assert c1.email == "ana@email.com"
    assert c1.vip == True
    print("✅ Cliente creado correctamente\n")

    # Test 2: __str__ para cliente VIP
    print("Test 2: __str__ para cliente VIP")
    str_c1 = str(c1)  # Llama a __str__
    print(f"str(c1) = {str_c1}")
    assert "Ana García" in str_c1
    assert "ana@email.com" in str_c1
    assert "VIP" in str_c1, "❌ Debe indicar que es VIP"
    print("✅ __str__ correcto para VIP\n")

    # Test 3: __str__ para cliente normal
    print("Test 3: __str__ para cliente normal")
    c2 = Cliente("Luis Pérez", "luis@email.com", False)
    str_c2 = str(c2)
    print(f"str(c2) = {str_c2}")
    assert "Luis Pérez" in str_c2
    assert "luis@email.com" in str_c2
    # No debe decir VIP si no lo es
    print("✅ __str__ correcto para cliente normal\n")

    # Test 4: __repr__
    print("Test 4: __repr__")
    repr_c1 = repr(c1)  # Llama a __repr__
    print(f"repr(c1) = {repr_c1}")
    assert "Cliente(" in repr_c1
    assert "nombre=" in repr_c1 or "nombre =" in repr_c1
    assert "Ana García" in repr_c1
    assert "vip=" in repr_c1 or "vip =" in repr_c1
    print("✅ __repr__ correcto\n")

    # Test 5: __eq__ - Clientes con mismo email son iguales
    print("Test 5: __eq__ - Igualdad por email")
    c3 = Cliente("Ana García López", "ana@email.com", False)  # Mismo email que c1
    assert c1 == c3, "❌ Clientes con mismo email deberían ser iguales"
    print(f"✅ {c1.nombre} == {c3.nombre} (mismo email)\n")

    # Test 6: __eq__ - Clientes con diferente email NO son iguales
    print("Test 6: __eq__ - Diferencia por email")
    assert c1 != c2, "❌ Clientes con diferente email NO deberían ser iguales"
    print(f"✅ {c1.nombre} != {c2.nombre} (diferente email)\n")

    print("🎉 ¡Todos los tests pasaron! Ejercicio 2 completado.\n")


if __name__ == "__main__":
    # Descomenta cuando termines:
    test_cliente()

    # Para probar manualmente:
    # c = Cliente("María López", "maria@email.com", True)
    # print(c)        # Llama a __str__
    # print(repr(c))  # Llama a __repr__
    pass
