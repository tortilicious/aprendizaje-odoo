# DÍA 7 - TEORÍA COMPLETA: LAMBDA, TYPE HINTS Y MÓDULOS

**Fecha:** 18/11/2025  
**Estudiante:** Miguel (DAM)  
**Objetivo:** Dominar Lambda, Type Hints y conceptos de Módulos para prepararse para Odoo

---

## 📚 TABLA DE CONTENIDOS

1. [Lambda](#lambda)
2. [Type Hints](#type-hints)
3. [Módulos y Paquetes](#módulos-y-paquetes)
4. [Comparación: map/filter/sorted vs List Comprehension](#comparación-mapfiltersorted-vs-list-comprehension)
5. [Diccionarios Avanzados: items(), keys(), values()](#diccionarios-avanzados)
6. [Resumen de Conceptos](#resumen-de-conceptos)

---

## LAMBDA

### ¿Qué es una Lambda?

Una **lambda** es una **función anónima pequeña** de una sola línea. Es útil cuando necesitas una función simple que solo usarás **una vez**.

**Sintaxis:**
```python
lambda parámetros: expresión_retorno
```

**Ejemplos básicos:**
```python
# Lambda simple
multiplicar = lambda x: x * 2
print(multiplicar(5))  # 10

# Lambda con múltiples parámetros
sumar = lambda x, y: x + y
print(sumar(3, 4))  # 7

# Lambda con condición
es_positivo = lambda x: x > 0
print(es_positivo(5))   # True
print(es_positivo(-3))  # False
```

---

### Limitación Clave de Lambda

**Las lambdas SOLO pueden tener UNA LÍNEA de código.**

```python
# ❌ NO FUNCIONA - Dos líneas
lambda x: print(f"Procesando {x}") 
          return x * 2

# ✅ FUNCIONA - Una línea
lambda x: x * 2

# ✅ FUNCIONA - Una línea compleja con if-else
lambda x: 10 if x >= 500 else 5 if x >= 200 else 0
```

Si necesitas lógica compleja, **usa una función normal:**

```python
def procesar(x):
    print(f"Procesando {x}")
    resultado = x * 2
    return resultado
```

---

### Cuándo Usar Lambda

**✅ USA LAMBDA cuando:**
- Necesitas una función simple, una línea
- La usarás solo una vez
- La pasarás a otra función (callback)

**❌ NO USES LAMBDA cuando:**
- Necesitas múltiples líneas de código
- La usarás varias veces (define una función normal)
- La lógica es compleja (usa una función normal para legibilidad)

---

### Lambda en Kotlin vs Python

**Kotlin (que ya conoces):**
```kotlin
numeros.map { it * 2 }           // { it * 2 }
numeros.filter { it > 5 }        // { it > 5 }
numeros.sortedBy { it }          // { it }
```

**Python (similar, sintaxis diferente):**
```python
list(map(lambda x: x * 2, numeros))              # lambda x: x * 2
list(filter(lambda x: x > 5, numeros))           # lambda x: x > 5
sorted(numeros, key=lambda x: x)                 # lambda x: x
```

---

### Casos de Uso Principales

#### 1. max() / min() con Lambda

```python
personas = [("Miguel", 25), ("Ana", 30), ("Carlos", 22)]

# Encontrar la persona más joven
mas_joven = min(personas, key=lambda x: x[1])
print(mas_joven)  # ('Carlos', 22)

# Encontrar la persona más vieja
mas_vieja = max(personas, key=lambda x: x[1])
print(mas_vieja)  # ('Ana', 30)
```

**Estructura:**
```
max(iterable, key=lambda x: x.atributo)
```

---

#### 2. sorted() con Lambda

```python
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 75},
]

# Ordenar por precio (ascendente)
por_precio = sorted(productos, key=lambda x: x["precio"])
# [Mouse($25), Teclado($75), Laptop($1200)]

# Ordenar por precio (descendente)
por_precio_desc = sorted(productos, key=lambda x: x["precio"], reverse=True)
# [Laptop($1200), Teclado($75), Mouse($25)]
```

**Estructura:**
```
sorted(iterable, key=lambda x: x.atributo, reverse=False)
```

---

#### 3. Lambda como Callback

Cuando pasas una lambda a otra función:

```python
def aplicar_operacion(numeros, operacion):
    """operacion es una función que se aplica a cada número"""
    return [operacion(x) for x in numeros]

# Uso con lambdas
resultado1 = aplicar_operacion([1, 2, 3], lambda x: x * 2)
print(resultado1)  # [2, 4, 6]

resultado2 = aplicar_operacion([1, 2, 3], lambda x: x ** 2)
print(resultado2)  # [1, 4, 9]
```

---

#### 4. Diccionarios Complejos con Lambda

```python
libros = [
    {"titulo": "1984", "autor": "Orwell", "precio": 1200},
    {"titulo": "Clean Code", "autor": "Martin", "precio": 75},
    {"titulo": "Python Pro", "autor": "Bader", "precio": 45},
]

# Libro más caro
mas_caro = max(libros, key=lambda x: x["precio"])
print(mas_caro["titulo"])  # "1984"

# Ordenar por autor
por_autor = sorted(libros, key=lambda x: x["autor"])
# [Python Pro (Bader), Clean Code (Martin), 1984 (Orwell)]

# Encontrar libro cuyo título es más largo
titulo_largo = max(libros, key=lambda x: len(x["titulo"]))
print(titulo_largo["titulo"])  # "Clean Code"
```

---

### Lambda con items() en Diccionarios

Este es un patrón **muy común y confuso**:

```python
productos = {
    "Laptop": {"precio": 1200, "stock": 5},
    "Mouse": {"precio": 25, "stock": 50},
}

# ❌ ESTO NO FUNCIONA (retorna el diccionario, no el nombre)
max(productos.values(), key=lambda x: x["precio"])
# Retorna: {'precio': 1200, 'stock': 5}

# ✅ ESTO FUNCIONA (retorna el nombre)
max(productos.items(), key=lambda x: x[1]["precio"])[0]
# Retorna: 'Laptop'
```

**¿Por qué?**

```python
# productos.values() solo da los valores
productos.values()
# [{'precio': 1200, 'stock': 5}, {'precio': 25, 'stock': 50}]

# productos.items() da tuplas (clave, valor)
productos.items()
# [('Laptop', {'precio': 1200, 'stock': 5}), 
#  ('Mouse', {'precio': 25, 'stock': 50})]

# En la tupla:
# x[0] = nombre ('Laptop')
# x[1] = diccionario ({'precio': 1200, 'stock': 5})
```

---

## TYPE HINTS

### ¿Qué son Type Hints?

**Type Hints** son anotaciones que indican **qué tipo de datos** espera una función y qué retorna.

En **Java/Kotlin es obligatorio**, en **Python es opcional pero recomendado**.

**Sintaxis:**
```python
def función(parámetro: Tipo) -> TipoRetorno:
    pass
```

---

### Type Hints Básicos

```python
# Función sin type hints (Python permite esto)
def sumar(a, b):
    return a + b

# Función con type hints (mejor)
def sumar(a: int, b: int) -> int:
    return a + b
```

**Tipos comunes:**
```python
def ejemplo(
    nombre: str,          # texto
    edad: int,            # número entero
    precio: float,        # número decimal
    activo: bool,         # verdadero/falso
    valor: None           # nada
) -> str:
    return f"{nombre} ({edad})"
```

---

### Type Hints con Colecciones

**Para listas, diccionarios, etc., necesitas importar de `typing`:**

```python
from typing import List, Dict, Set, Tuple, Optional

# Lista de enteros
def sumar_numeros(numeros: List[int]) -> int:
    return sum(numeros)

# Diccionario con strings como claves y int como valores
def contar_elementos(datos: Dict[str, int]) -> int:
    return sum(datos.values())

# Tupla de dos elementos
def obtener_coordenadas() -> Tuple[int, int]:
    return (10, 20)

# Conjunto de strings
def obtener_colores() -> Set[str]:
    return {"rojo", "azul", "verde"}
```

---

### Optional - Cuando algo puede ser None

```python
from typing import Optional

# Función que puede retornar un número o None
def dividir(a: int, b: int) -> Optional[int]:
    if b == 0:
        return None
    return a // b

# Búsqueda que puede no encontrar nada
def buscar_usuario(usuarios: List[Dict], id: int) -> Optional[Dict]:
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None
```

---

### Type Hints en Clases

```python
class Libro:
    def __init__(self, id: int, titulo: str, precio: float) -> None:
        self.id: int = id
        self.titulo: str = titulo
        self.precio: float = precio
    
    def __repr__(self) -> str:
        return f"Libro({self.titulo}, ${self.precio})"
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        return self.precio * (1 - porcentaje / 100)
```

---

### Ventajas de Type Hints

1. **Autocomplete mejorado** en PyCharm
2. **Detección de errores** antes de ejecutar
3. **Documentación clara** (se ve qué tipo espera)
4. **Código profesional** (como Java/Kotlin)
5. **Herramientas de análisis** pueden verificar tipos

---

## MÓDULOS Y PAQUETES

### ¿Qué es un Módulo?

Un **módulo** es simplemente un archivo `.py`.

```
dia_7/
  ├─ mi_modulo.py  ← Esto es un módulo
  └─ main.py       ← Esto es otro módulo
```

---

### ¿Qué es un Paquete?

Un **paquete** es una **carpeta que contiene módulos y un archivo `__init__.py`**.

```
dia_7/
  ├─ proyecto_completo/      ← Esto es un paquete
  │   ├─ __init__.py         ← Indica que es paquete
  │   ├─ modelos.py          ← Módulo
  │   ├─ operaciones.py      ← Módulo
  │   └─ main.py             ← Módulo
  └─ otro_modulo.py          ← Módulo simple
```

---

### `__init__.py` - El archivo mágico

El archivo `__init__.py` **hace que Python reconozca una carpeta como paquete**.

Puede estar vacío:
```python
# __init__.py vacío - eso es suficiente
```

O contener código:
```python
# __init__.py con código
from .modelos import Producto
from .operaciones import TiendaOperaciones

__all__ = ['Producto', 'TiendaOperaciones']
```

---

### Cómo Importar Módulos

**Importar todo de un módulo:**
```python
from modelos import Producto, Cliente
```

**Importar un módulo entero:**
```python
import modelos
# Uso: modelos.Producto(...)
```

**Importar con alias:**
```python
from modelos import Producto as Prod
```

---

### Estructura Recomendada

```
proyecto/
  ├─ __init__.py              # Paquete principal
  ├─ modelos.py               # Clases: Producto, Cliente, etc.
  ├─ operaciones.py           # Lógica: búsquedas, filtros, etc.
  ├─ main.py                  # Ejecución principal
  └─ utils.py                 # Funciones auxiliares (opcional)
```

**Regla de oro:** Cada archivo tiene **una responsabilidad**:
- `modelos.py` → Define qué SON las cosas
- `operaciones.py` → Define QUÉ HACER con esas cosas
- `main.py` → Ejecuta el programa

---

## COMPARACIÓN: map/filter/sorted vs List Comprehension

Este es un tema **muy importante**. Python tiene varias formas de hacer lo mismo, pero algunas son mejores que otras.

### map() vs List Comprehension

**Caso: Multiplicar cada número por 2**

```python
numeros = [1, 2, 3, 4, 5]

# Forma 1: map + lambda
resultado1 = list(map(lambda x: x * 2, numeros))

# Forma 2: list comprehension
resultado2 = [x * 2 for x in numeros]

# Ambas retornan: [2, 4, 6, 8, 10]
```

**¿Cuál usar?**

| Criterio | map + lambda | List Comprehension |
|----------|-------------|-------------------|
| Legibilidad | ❌ Confusa | ✅ Muy clara |
| Rendimiento | ✅ Ligeramente mejor | ✅ Similar |
| Recomendado | ⚠️ Rara vez | ✅ Casi siempre |

**Recomendación:** **Usa list comprehension para map**, `map()` es menos pythónico.

---

### filter() vs List Comprehension

**Caso: Filtrar números mayores a 3**

```python
numeros = [1, 2, 3, 4, 5]

# Forma 1: filter + lambda
resultado1 = list(filter(lambda x: x > 3, numeros))

# Forma 2: list comprehension
resultado2 = [x for x in numeros if x > 3]

# Ambas retornan: [4, 5]
```

**¿Cuál usar?**

| Criterio | filter + lambda | List Comprehension |
|----------|-----------------|-------------------|
| Legibilidad | ❌ Confusa | ✅ Muy clara |
| Rendimiento | ✅ Similar | ✅ Similar |
| Recomendado | ⚠️ Rara vez | ✅ Casi siempre |

**Recomendación:** **Usa list comprehension para filter**.

---

### sorted() + key

**Caso: Ordenar por precio**

```python
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
]

# Forma 1: sorted + lambda
resultado1 = sorted(productos, key=lambda x: x["precio"])

# Forma 2: list comprehension (❌ NO FUNCIONA para ordenar)
# No hay forma de hacer esto con list comprehension
```

**¿Cuál usar?**

- **`sorted()` con `key=lambda` es OBLIGATORIO** para ordenamientos
- No hay alternativa con list comprehension

**Recomendación:** **Siempre usa `sorted()` para ordenamientos**.

---

### max() / min() + key

**Caso: Encontrar el producto más caro**

```python
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
]

# Forma 1: max + lambda
mas_caro = max(productos, key=lambda x: x["precio"])

# Forma 2: list comprehension (❌ NO FUNCIONA para encontrar máximo)
# No hay forma de hacer esto con list comprehension
```

**Recomendación:** **Siempre usa `max()` / `min()` para encontrar extremos**.

---

### TABLA RESUMEN

| Operación | Herramienta | Alternativa | Recomendación |
|-----------|-------------|------------|---------------|
| Transformar (map) | `map() + lambda` | List comprehension | ✅ Usa comprehension |
| Filtrar | `filter() + lambda` | List comprehension | ✅ Usa comprehension |
| Ordenar | `sorted() + key=lambda` | Ninguna | ✅ Usa sorted |
| Máximo/Mínimo | `max/min + key=lambda` | Ninguna | ✅ Usa max/min |

---

### REGLA DE ORO

**Siempre que puedas hacer algo con list comprehension, usa list comprehension.**

Los únicos casos donde NO puedes usar list comprehension son:
- **Ordenamientos** → Usa `sorted()`
- **Encontrar máximo/mínimo** → Usa `max()` / `min()`
- **Operaciones complejas** → Usa una función normal

---

## DICCIONARIOS AVANZADOS

### métodos principales

#### 1. items() - Tuplas (clave, valor)

```python
producto = {"nombre": "Laptop", "precio": 1200, "stock": 5}

# Retorna tuplas
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

# Output:
# nombre: Laptop
# precio: 1200
# stock: 5
```

---

#### 2. keys() - Solo claves

```python
producto = {"nombre": "Laptop", "precio": 1200}

claves = producto.keys()
print(claves)  # dict_keys(['nombre', 'precio'])

# Convertir a lista si necesitas
claves_lista = list(producto.keys())
print(claves_lista)  # ['nombre', 'precio']
```

---

#### 3. values() - Solo valores

```python
producto = {"nombre": "Laptop", "precio": 1200}

valores = producto.values()
print(valores)  # dict_values(['Laptop', 1200])

# Sumar valores si son números
inventario = {"Laptop": 5, "Mouse": 50, "Teclado": 15}
total = sum(inventario.values())
print(total)  # 70
```

---

#### 4. get() - Acceso seguro

```python
producto = {"nombre": "Laptop", "precio": 1200}

# Sin get (puede dar error)
# print(producto["color"])  # ❌ KeyError

# Con get (seguro)
color = producto.get("color")
print(color)  # None (sin error)

# Con valor por defecto
color = producto.get("color", "Sin especificar")
print(color)  # "Sin especificar"
```

---

#### 5. setdefault() - Añadir con valor por defecto

```python
producto = {"nombre": "Laptop"}

# Si no existe "precio", lo añade
producto.setdefault("precio", 0)
print(producto)  # {'nombre': 'Laptop', 'precio': 0}

# Si existe, no cambia
producto.setdefault("precio", 1000)
print(producto)  # {'nombre': 'Laptop', 'precio': 0} (sin cambios)
```

---

### Diccionarios Anidados con Lambda

```python
datos = {
    "productos": {
        "Laptop": {"precio": 1200, "stock": 5},
        "Mouse": {"precio": 25, "stock": 50},
    }
}

# Acceder a valores anidados
precios = datos["productos"].values()
max_precio = max(precios, key=lambda x: x["precio"])
print(max_precio)  # {'precio': 1200, 'stock': 5}

# Con items() para obtener el nombre también
producto_caro = max(datos["productos"].items(), 
                    key=lambda x: x[1]["precio"])[0]
print(producto_caro)  # 'Laptop'
```

---

## RESUMEN DE CONCEPTOS

### Lambda en una frase
**Función anónima pequeña de una línea, usada cuando la necesitas una sola vez.**

### Type Hints en una frase
**Anotaciones que indican qué tipo de datos espera una función y qué retorna.**

### Módulos en una frase
**Archivos Python organizados en carpetas (paquetes) para separar responsabilidades.**

---

### Cuándo usar cada herramienta

| Herramienta | Cuándo | Ejemplo |
|-------------|--------|---------|
| Lambda | Función simple, una línea, usada una vez | `sorted(lista, key=lambda x: x["precio"])` |
| Type Hints | Siempre (código profesional) | `def suma(a: int, b: int) -> int:` |
| Módulos | Proyectos con más de 100 líneas | Separar `modelos.py` de `operaciones.py` |
| List Comprehension | Filtrar o transformar listas | `[x for x in lista if x > 5]` |
| sorted() | Ordenar por criterio personalizado | `sorted(lista, key=lambda x: x.precio)` |
| max() / min() | Encontrar extremos | `max(lista, key=lambda x: x.edad)` |

---

### Errores Comunes

**❌ Usar lambda para lógica compleja:**
```python
# No hagas esto
lambda x: x * 2 if x > 10 else x / 2 if x > 5 else x
```

**✅ Usa una función normal:**
```python
def procesar(x):
    if x > 10:
        return x * 2
    elif x > 5:
        return x / 2
    else:
        return x
```

---

**❌ No usar type hints:**
```python
def sumar(a, b):
    return a + b
```

**✅ Siempre añade type hints:**
```python
def sumar(a: int, b: int) -> int:
    return a + b
```

---

**❌ Mezclar map/filter cuando puedes usar comprehension:**
```python
list(map(lambda x: x * 2, list(filter(lambda x: x > 5, lista))))
```

**✅ Usa list comprehension:**
```python
[x * 2 for x in lista if x > 5]
```

---

## CONEXIÓN CON ODOO

Cuando comiences con Odoo, verás:

✅ **Decoradores con parámetros** (parecido a lambda como callbacks):
```python
@api.depends('campo1', 'campo2')
def _compute_total(self):
    pass
```

✅ **Type Hints** (Odoo 16+ lo usa):
```python
def metodo(self, ids: List[int]) -> Dict:
    pass
```

✅ **Diccionarios complejos** (vals, context, domain):
```python
vals = {
    "nombre": "Producto",
    "precio": 100,
}
```

✅ **List Comprehension y sorted()**:
```python
productos_activos = [p for p in self.env['product.product'].search([]) 
                     if p.active]
```

---

## CHECKLIST FINAL

- [x] Entiendo qué es una lambda y cuándo usarla
- [x] Entiendo max(), min(), sorted() con key=lambda
- [x] Entiendo type hints básicos y complejos
- [x] Entiendo List Comprehension vs map/filter
- [x] Entiendo módulos y paquetes
- [x] Entiendo diccionarios.items(), keys(), values()
- [x] Puedo escribir código profesional con type hints
- [x] Sé cuándo usar cada herramienta

---

**Este documento es tu referencia. Guárdalo y revísalo cuando sea necesario.**

**¡Estás listo para el Día 7 y para Odoo! 🚀**