"""
EJERCICIO 4: Herencia Simple

Objetivo: Crear jerarquía de clases con herencia y sobrescritura de métodos

CONCEPTOS:
- Clase padre (base)
- Clase hija (derivada)
- super() para llamar al constructor/métodos del padre
- Sobrescritura de métodos (@Override en Java)

COMPARACIÓN CON JAVA:
Java:                                   Python:
public class Empleado { }               class Empleado:
                                            def __init__(self, ...):
public class Gerente
    extends Empleado {                  class Gerente(Empleado):
                                            def __init__(self, ...):
    public Gerente(...) {                       super().__init__(...)
        super(...);
    }

    @Override                               def calcular_salario(self):
    public double calcularSalario() {           salario_base = super().calcular_salario()
        // ...                                   return salario_base + self.bono
    }
}

DIFERENCIAS:
- Python: class Hija(Padre)
- Java: class Hija extends Padre
- super() en Python no lleva parámetros
"""


# TODO: Crear las siguientes clases:

# 1. Clase Empleado (PADRE):
#    - Constructor: nombre (str), salario_base (float)
#    - Método calcular_salario(): retorna salario_base
#    - Método __str__: "Empleado: [nombre] - Salario: [salario]€"

# 2. Clase Gerente (HIJO de Empleado):
#    - Constructor: nombre, salario_base, bono (float)
#    - DEBE llamar a super().__init__() para el constructor padre
#    - Sobrescribir calcular_salario(): retorna salario_base + bono
#    - Sobrescribir __str__: "Gerente: [nombre] - Salario: [salario]€ (Bono: [bono]€)"

# 3. Clase Desarrollador (HIJO de Empleado):
#    - Constructor: nombre, salario_base, lenguaje (str)
#    - DEBE llamar a super().__init__()
#    - Sobrescribir calcular_salario():
#      * Si lenguaje es "Python": salario_base * 1.1 (10% extra)
#      * Si no: salario_base normal
#    - Sobrescribir __str__: "Desarrollador [lenguaje]: [nombre] - Salario: [salario]€"

class Empleado:
    """Clase base para todos los empleados"""

    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def __str__(self):
        return f"Empleado: {self.nombre} - Salario: {self.salario_base}€"

    def calcular_salario(self):
        return self.salario_base


class Gerente(Empleado):
    """Gerente con bono adicional"""
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def __str__(self):
        return f"Gerente: {self.nombre} - Salario: {self.salario_base}€ (Bono: {self.bono}€)"

    def calcular_salario(self):
        salario = super().calcular_salario()
        return salario + self.bono


class Desarrollador(Empleado):
    """Desarrollador con especialización en un lenguaje"""
    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def __str__(self):
        return f"Desarrollador {self.lenguaje}: {self.nombre} - Salario: {self.salario_base}€"

    def calcular_salario(self):
        salario_base = super().calcular_salario()
        if self.lenguaje == "Python":
            return salario_base * 1.1
        return salario_base


# ============================================================================
# TESTS - No modificar
# ============================================================================

def test_herencia():
    """Tests automáticos para validar tu implementación"""
    print("🧪 Ejecutando tests del Ejercicio 4...\n")

    # Test 1: Empleado base
    print("Test 1: Clase Empleado (base)")
    emp = Empleado("Juan Pérez", 2000.0)
    assert emp.nombre == "Juan Pérez"
    assert emp.salario_base == 2000.0
    assert emp.calcular_salario() == 2000.0
    print(f"✅ {emp}\n")

    # Test 2: Gerente hereda de Empleado
    print("Test 2: Clase Gerente (herencia)")
    gerente = Gerente("Ana García", 3000.0, 500.0)
    assert gerente.nombre == "Ana García", "❌ Gerente debe heredar 'nombre'"
    assert gerente.salario_base == 3000.0, "❌ Gerente debe heredar 'salario_base'"
    assert gerente.bono == 500.0
    print(f"✅ Gerente creado correctamente\n")

    # Test 3: Gerente sobrescribe calcular_salario()
    print("Test 3: Gerente sobrescribe calcular_salario()")
    salario_total = gerente.calcular_salario()
    assert salario_total == 3500.0, f"❌ Salario debería ser 3000+500=3500, no {salario_total}"
    print(f"✅ Salario calculado: {salario_total}€ (base + bono)\n")

    # Test 4: Gerente sobrescribe __str__
    print("Test 4: Gerente sobrescribe __str__()")
    str_gerente = str(gerente)
    assert "Gerente" in str_gerente or "gerente" in str_gerente.lower()
    assert "Ana García" in str_gerente
    print(f"✅ {str_gerente}\n")

    # Test 5: Desarrollador Python (con bonus)
    print("Test 5: Desarrollador Python (con bonus)")
    dev_python = Desarrollador("Luis Martínez", 2500.0, "Python")
    assert dev_python.lenguaje == "Python"
    salario_python = dev_python.calcular_salario()
    assert salario_python == 2750.0, f"❌ Salario Python debería ser 2500*1.1=2750, no {salario_python}"
    print(f"✅ {dev_python}")
    print(f"   Salario con bonus Python: {salario_python}€\n")

    # Test 6: Desarrollador Java (sin bonus)
    print("Test 6: Desarrollador Java (sin bonus)")
    dev_java = Desarrollador("María López", 2500.0, "Java")
    salario_java = dev_java.calcular_salario()
    assert salario_java == 2500.0, "❌ Desarrolladores no-Python no tienen bonus"
    print(f"✅ {dev_java}")
    print(f"   Salario sin bonus: {salario_java}€\n")

    # Test 7: isinstance() - Verificar herencia
    print("Test 7: isinstance() - Verificar jerarquía")
    assert isinstance(gerente, Empleado), "❌ Gerente debería ser instancia de Empleado"
    assert isinstance(dev_python, Empleado), "❌ Desarrollador debería ser instancia de Empleado"
    assert not isinstance(emp, Gerente), "❌ Empleado NO es instancia de Gerente"
    print("✅ Jerarquía de herencia correcta\n")

    print("🎉 ¡Todos los tests pasaron! Ejercicio 4 completado.\n")


if __name__ == "__main__":
    # Descomenta cuando termines:
    test_herencia()

    # Para probar manualmente:
    # emp = Empleado("Pedro", 2000)
    # print(emp)
    # gerente = Gerente("Ana", 3000, 500)
    # print(gerente)
    # print(f"Salario gerente: {gerente.calcular_salario()}€")
    pass
