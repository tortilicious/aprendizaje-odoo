# 🔄 Cheat Sheet: Java/Kotlin → Python (POO)

## 📌 Referencia Rápida para Programadores Java

### 1️⃣ Definición de Clase

**Java:**
```java
public class Producto {
    private String nombre;
    private double precio;
    
    // Constructor
    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }
    
    // Getter
    public String getNombre() {
        return nombre;
    }
    
    // Setter
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    // Método
    public double calcularIVA() {
        return precio * 1.21;
    }
}
```

**Python:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    # Getter (pythónico con @property)
    @property
    def nombre(self):
        return self._nombre
    
    # Setter (pythónico)
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    # Método
    def calcular_iva(self):
        return self.precio * 1.21
```

**Diferencias clave:**
- ❌ No hay `public`, `private`, `protected`
- ✅ `self` es obligatorio (≈ `this` en Java)
- ✅ No se declaran tipos
- ✅ `@property` reemplaza `get/set`
- ✅ Nombres de métodos: `snake_case` (no `camelCase`)

---

### 2️⃣ Métodos Especiales

**Java:**
```java
@Override
public String toString() {
    return "Producto: " + nombre;
}

@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (obj == null || getClass() != obj.getClass()) 
        return false;
    Producto p = (Producto) obj;
    return precio == p.precio && 
           nombre.equals(p.nombre);
}
```

**Python:**
```python
def __str__(self):
    return f"Producto: {self.nombre}"

def __repr__(self):
    return f"Producto(nombre='{self.nombre}', precio={self.precio})"

def __eq__(self, otro):
    return (self.precio == otro.precio and 
            self.nombre == otro.nombre)
```

**Tabla de equivalencias:**
| Java | Python | Uso |
|------|--------|-----|
| `toString()` | `__str__()` | Representación legible |
| (ninguno) | `__repr__()` | Representación técnica |
| `equals()` | `__eq__()` | Igualdad (`==`) |
| `hashCode()` | `__hash__()` | Hash |
| `compareTo()` | `__lt__()`, `__gt__()` | Comparación |

---

### 3️⃣ Herencia

**Java:**
```java
public class ProductoElectronico extends Producto {
    private int garantiaMeses;
    
    public ProductoElectronico(String nombre, 
                               double precio, 
                               int garantiaMeses) {
        super(nombre, precio);
        this.garantiaMeses = garantiaMeses;
    }
    
    @Override
    public double calcularIVA() {
        // Llama al método del padre
        double ivaBase = super.calcularIVA();
        return ivaBase + 10; // Extra
    }
}
```

**Python:**
```python
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)
        self.garantia_meses = garantia_meses
    
    def calcular_iva(self):
        # Llama al método del padre
        iva_base = super().calcular_iva()
        return iva_base + 10  # Extra
```

**Diferencias:**
- Java: `extends` → Python: `(ClasePadre)`
- Java: `super(args)` → Python: `super().__init__(args)`
- ✅ Herencia múltiple ES POSIBLE en Python (no en Java)

---

### 4️⃣ Propiedades (Getters/Setters)

**Java (estilo tradicional):**
```java
private double precio;

public double getPrecio() {
    return precio;
}

public void setPrecio(double precio) {
    if (precio < 0) {
        throw new IllegalArgumentException("Precio negativo");
    }
    this.precio = precio;
}

// USO:
producto.getPrecio();
producto.setPrecio(100);
```

**Python (pythónico con @property):**
```python
def __init__(self, precio):
    self._precio = precio  # Convención: _ = privado

@property
def precio(self):
    return self._precio

@precio.setter
def precio(self, valor):
    if valor < 0:
        raise ValueError("Precio negativo")
    self._precio = valor

# USO:
producto.precio        # Getter (sin paréntesis!)
producto.precio = 100  # Setter (como atributo!)
```

**Ventaja Python:** Se accede como atributo pero ejecuta código.

---

### 5️⃣ Atributos de Clase (Static)

**Java:**
```java
public class Producto {
    public static final double IVA = 0.21;
    private static int contador = 0;
    
    public Producto() {
        contador++;
    }
    
    public static int getContador() {
        return contador;
    }
}

// USO:
Producto.IVA;
Producto.getContador();
```

**Python:**
```python
class Producto:
    IVA = 0.21           # Atributo de clase (sin static)
    _contador = 0        # Atributo de clase
    
    def __init__(self):
        Producto._contador += 1
    
    @classmethod
    def get_contador(cls):
        return cls._contador
    
    @staticmethod
    def validar_precio(precio):
        return precio > 0

# USO:
Producto.IVA
Producto.get_contador()
Producto.validar_precio(100)
```

**Decoradores Python:**
- `@classmethod` ≈ método que recibe la clase
- `@staticmethod` ≈ `static` en Java
- No hay `final` (convención: MAYÚSCULAS = constante)

---

### 6️⃣ Modificadores de Acceso

**Java:**
```java
public class Producto {
    public String nombre;       // Público
    protected double precio;    // Protegido
    private int stock;          // Privado
}
```

**Python (solo convenciones):**
```python
class Producto:
    def __init__(self):
        self.nombre = "X"      # Público (por defecto)
        self._precio = 0       # "Privado" (convención)
        self.__stock = 0       # Name mangling (más privado)
```

**IMPORTANTE:**
- Python NO tiene modificadores reales
- `_atributo` = "por favor no lo uses" (convención)
- `__atributo` = name mangling (se renombra a `_Clase__atributo`)
- Todo es técnicamente accesible

---

### 7️⃣ Interfaces y Clases Abstractas

**Java:**
```java
public interface Vendible {
    double calcularPrecioFinal();
}

public abstract class Producto {
    public abstract double calcularIVA();
}

public class Libro extends Producto implements Vendible {
    @Override
    public double calcularIVA() { /* ... */ }
    
    @Override
    public double calcularPrecioFinal() { /* ... */ }
}
```

**Python (módulo abc):**
```python
from abc import ABC, abstractmethod

class Vendible(ABC):
    @abstractmethod
    def calcular_precio_final(self):
        pass

class Producto(ABC):
    @abstractmethod
    def calcular_iva(self):
        pass

class Libro(Producto, Vendible):  # Herencia múltiple!
    def calcular_iva(self):
        # Implementación
        pass
    
    def calcular_precio_final(self):
        # Implementación
        pass
```

**Diferencia:** Python permite herencia múltiple (interfaces ≈ clases)

---

## 🎯 Resumen de Diferencias Clave

| Aspecto | Java | Python |
|---------|------|--------|
| **Declaración clase** | `public class X {}` | `class X:` |
| **Constructor** | `public X() {}` | `def __init__(self):` |
| **This/Self** | `this` (opcional) | `self` (obligatorio) |
| **Privacidad** | `private`, `public` | `_attr` (convención) |
| **Getters/Setters** | `getX()`, `setX()` | `@property` |
| **toString()** | `toString()` | `__str__()` |
| **equals()** | `equals()` | `__eq__()` |
| **Herencia** | `extends` | `(ClasePadre)` |
| **Super** | `super(args)` | `super().__init__(args)` |
| **Static** | `static` | `@staticmethod` |
| **Herencia múltiple** | ❌ No | ✅ Sí |
| **Interfaces** | `interface` | Clases abstractas |
| **Tipos** | Obligatorios | Opcionales (duck typing) |
| **Bloques** | `{ }` | Indentación |

---

## 🔥 Errores Comunes Java → Python

### ❌ Olvidar `self`
```python
# ❌ Error
def metodo():
    return nombre

# ✅ Correcto
def metodo(self):
    return self.nombre
```

### ❌ Usar sintaxis Java
```python
# ❌ Error (estilo Java)
def getNombre(self):
    return self.nombre

# ✅ Correcto (pythónico)
@property
def nombre(self):
    return self._nombre
```

### ❌ Declarar tipos
```python
# ❌ Error (no se hace así)
private String nombre;
int edad = 0;

# ✅ Correcto
self.nombre = ""
self.edad = 0
```

### ❌ Olvidar `self` al asignar
```python
# ❌ Error (variable local, no atributo)
def __init__(self, nombre):
    nombre = nombre

# ✅ Correcto
def __init__(self, nombre):
    self.nombre = nombre
```

---

## 💡 Consejos para la Transición

1. **Olvida los tipos**: Python es dinámico
2. **Usa `@property`**: Más elegante que get/set
3. **self es obligatorio**: Siempre primer parámetro
4. **snake_case**: Para métodos (no camelCase)
5. **Indentación**: Reemplaza llaves
6. **Todo es público**: Solo convenciones con `_`
7. **Duck typing**: "Si camina como pato, es un pato"

---

**📌 Guarda este archivo como referencia rápida!**
