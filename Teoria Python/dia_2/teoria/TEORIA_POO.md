# 🎓 Teoría POO en Python - Día 2

## 📚 Comparación Java/Kotlin → Python

### 1. Definición de Clases

**Java:**
```java
public class Producto {
    private String nombre;
    private double precio;
    
    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }
}
```

**Python:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
```

**Diferencias clave:**
- ❌ No hay `public`, `private`, `protected` (por convención, `_atributo` es privado)
- ❌ No se declaran tipos de atributos
- ✅ `self` es equivalente a `this` (pero es obligatorio como primer parámetro)
- ✅ `__init__` es el constructor (doble guión bajo)

---

### 2. Atributos de Clase vs Instancia

**Python:**
```python
class Producto:
    # Atributo de CLASE (compartido por todas las instancias)
    iva = 0.21
    contador = 0
    
    def __init__(self, nombre, precio):
        # Atributos de INSTANCIA (únicos por objeto)
        self.nombre = nombre
        self.precio = precio
        Producto.contador += 1
```

**Java equivalente:**
```java
public class Producto {
    // Atributo de clase (static)
    public static double IVA = 0.21;
    public static int contador = 0;
    
    // Atributos de instancia
    private String nombre;
    private double precio;
}
```

---

### 3. Métodos

**Python:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    # Método de INSTANCIA (siempre recibe self)
    def calcular_precio_con_iva(self):
        return self.precio * 1.21
    
    # Método de CLASE (recibe la clase, no la instancia)
    @classmethod
    def crear_desde_texto(cls, texto):
        nombre, precio = texto.split(",")
        return cls(nombre, float(precio))
    
    # Método ESTÁTICO (no recibe ni self ni cls)
    @staticmethod
    def validar_precio(precio):
        return precio > 0
```

**Java equivalente:**
```java
public class Producto {
    // Método de instancia
    public double calcularPrecioConIva() {
        return this.precio * 1.21;
    }
    
    // Método estático
    public static boolean validarPrecio(double precio) {
        return precio > 0;
    }
}
```

---

### 4. Métodos Especiales (Magic Methods)

Python tiene métodos con doble guión bajo (`__method__`) para operaciones especiales:

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    # Representación en string (para print)
    def __str__(self):
        return f"Producto: {self.nombre} - {self.precio}€"
    
    # Representación técnica (para debug)
    def __repr__(self):
        return f"Producto(nombre='{self.nombre}', precio={self.precio})"
    
    # Comparación de igualdad
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.precio == otro.precio
    
    # Comparación menor que
    def __lt__(self, otro):
        return self.precio < otro.precio
    
    # Longitud (si aplica)
    def __len__(self):
        return len(self.nombre)
```

**Java equivalente:**
```java
@Override
public String toString() {
    return "Producto: " + nombre + " - " + precio + "€";
}

@Override
public boolean equals(Object obj) {
    // ...
}
```

---

### 5. Propiedades con @property

**Python:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Convención: _ indica "privado"
        self._precio = precio
    
    # GETTER (acceso como atributo)
    @property
    def nombre(self):
        return self._nombre
    
    # SETTER (asignación como atributo)
    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("Nombre no puede estar vacío")
        self._nombre = valor
    
    @property
    def precio_con_iva(self):
        return self._precio * 1.21

# USO:
p = Producto("Laptop", 1000)
print(p.nombre)           # Llama al getter (no hace falta p.nombre())
p.nombre = "PC"           # Llama al setter
print(p.precio_con_iva)   # Propiedad calculada (solo getter)
```

**Java equivalente:**
```java
private String nombre;

public String getNombre() {
    return nombre;
}

public void setNombre(String valor) {
    if (valor.isEmpty()) {
        throw new IllegalArgumentException("...");
    }
    this.nombre = valor;
}

// USO:
p.getNombre();
p.setNombre("PC");
```

**Ventaja Python:** Se accede como atributo pero se ejecuta código de validación.

---

### 6. Herencia

**Python:**
```python
# Clase padre
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_info(self):
        return f"{self.nombre}: {self.precio}€"

# Clase hija
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)  # Llamar constructor padre
        self.garantia_meses = garantia_meses
    
    # Sobrescribir método
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} (Garantía: {self.garantia_meses} meses)"
```

**Java equivalente:**
```java
public class ProductoElectronico extends Producto {
    private int garantiaMeses;
    
    public ProductoElectronico(String nombre, double precio, int garantiaMeses) {
        super(nombre, precio);
        this.garantiaMeses = garantiaMeses;
    }
    
    @Override
    public String mostrarInfo() {
        // ...
    }
}
```

---

### 7. Herencia Múltiple (NO existe en Java)

**Python permite herencia múltiple:**
```python
class Vendible:
    def vender(self):
        return "Producto vendido"

class Transportable:
    def transportar(self):
        return "Producto en camino"

class ProductoFisico(Vendible, Transportable):
    def __init__(self, nombre):
        self.nombre = nombre

# USO:
p = ProductoFisico("Silla")
p.vender()        # ✅ Método de Vendible
p.transportar()   # ✅ Método de Transportable
```

---

## 🎯 Convenciones Python

### Nombres:
- **Clases:** `PascalCase` (como Java)
- **Métodos/funciones:** `snake_case` (diferente de Java)
- **Constantes:** `MAYUSCULAS_CON_GUIONES`
- **Privado (convención):** `_atributo` o `__atributo`

### Privacidad:
- Python NO tiene modificadores de acceso reales
- Convención: `_atributo` es "privado por favor no lo uses"
- `__atributo` causa name mangling (se renombra a `_Clase__atributo`)

---

## 📊 Resumen de Diferencias

| Concepto | Java/Kotlin | Python |
|----------|-------------|--------|
| Constructor | `public Clase()` | `def __init__(self)` |
| This | `this` | `self` (obligatorio) |
| Herencia | `extends` | `(ClasePadre)` |
| Privado | `private` | `_atributo` (convención) |
| Getter/Setter | `getNombre()` | `@property` |
| toString() | `toString()` | `__str__()` |
| equals() | `equals()` | `__eq__()` |
| Static | `static` | `@staticmethod` |
| Herencia múltiple | ❌ No | ✅ Sí |

---

## 🔑 Conceptos Clave

1. **Todo es público por defecto** (solo convenciones)
2. **self es obligatorio** en métodos de instancia
3. **@property** = getters/setters pythónicos
4. **Métodos especiales** (`__str__`, `__eq__`, etc.) son muy importantes
5. **super()** funciona similar a Java pero sin parámetros
6. **Herencia múltiple** es posible y útil

---

## ✅ Ready para los Ejercicios

Ahora que conoces la teoría, vamos a los ejercicios prácticos donde:
- Crearás clases desde cero
- Implementarás métodos especiales
- Usarás herencia
- Aplicarás @property
- Construirás un sistema completo

**¡Manos a la obra! 🚀**
