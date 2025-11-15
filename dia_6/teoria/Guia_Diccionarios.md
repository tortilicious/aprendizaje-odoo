# Operaciones Avanzadas de Diccionarios en Python

## 1. Conceptos Fundamentales

### ¿Qué es un diccionario?

Un diccionario es una colección de pares **clave-valor**. Es como una tabla de búsqueda rápida.

```python
persona = {
    "nombre": "Miguel",
    "edad": 20,
    "ciudad": "Madrid"
}

print(persona["nombre"])  # Miguel
```

### ¿Por qué "avanzado"?

No es solo acceder a valores. Se trata de:
- Manipular estructuras complejas
- Trabajar con diccionarios anidados
- Operaciones de transformación y filtrado
- Manejo eficiente de datos

---

## 2. Acceso y Modificación Segura

### El problema: KeyError

```python
diccionario = {"a": 1, "b": 2}
print(diccionario["c"])  # KeyError: 'c'
```

### Solución 1: `.get()`

```python
diccionario = {"a": 1, "b": 2}
print(diccionario.get("c"))  # None (no error)
print(diccionario.get("c", "valor_defecto"))  # valor_defecto
```

### Solución 2: `.setdefault()`

Similar a `get()`, pero **también añade la clave si no existe**:

```python
diccionario = {"a": 1}
valor = diccionario.setdefault("b", 2)
print(valor)  # 2
print(diccionario)  # {'a': 1, 'b': 2}
```

### Solución 3: `in` para verificar existencia

```python
diccionario = {"a": 1}
if "a" in diccionario:
    print("La clave existe")
```

---

## 3. Iteración Avanzada

### Acceder a claves

```python
persona = {"nombre": "Miguel", "edad": 20}
for clave in persona:
    print(clave)
# nombre
# edad
```

### Acceder a valores

```python
for valor in persona.values():
    print(valor)
# Miguel
# 20
```

### Acceder a pares clave-valor

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# nombre: Miguel
# edad: 20
```

---

## 4. Diccionarios Anidados

### Estructura

```python
estudiantes = {
    "miguel": {
        "edad": 20,
        "calificaciones": [8.5, 9.0, 7.5]
    },
    "ana": {
        "edad": 21,
        "calificaciones": [9.5, 8.0, 9.0]
    }
}
```

### Acceso

```python
# Primer nivel
print(estudiantes["miguel"])  # {'edad': 20, 'calificaciones': [...]}

# Segundo nivel
print(estudiantes["miguel"]["edad"])  # 20

# Acceso a listas dentro de dicts
print(estudiantes["miguel"]["calificaciones"][0])  # 8.5
```

### Modificación

```python
# Agregar datos anidados
estudiantes["miguel"]["ciudad"] = "Madrid"

# Modificar datos anidados
estudiantes["miguel"]["edad"] = 21

# Agregar elemento a lista anidada
estudiantes["miguel"]["calificaciones"].append(8.0)
```

---

## 5. Métodos Útiles

### `.keys()`, `.values()`, `.items()`

```python
diccionario = {"a": 1, "b": 2}

print(diccionario.keys())    # dict_keys(['a', 'b'])
print(diccionario.values())  # dict_values([1, 2])
print(diccionario.items())   # dict_items([('a', 1), ('b', 2)])
```

Útil para:
```python
# Convertir a listas
claves = list(diccionario.keys())
valores = list(diccionario.values())

# Usar en bucles
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
```

### `.update()`

Fusionar diccionarios:

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

Si hay claves duplicadas, se sobrescriben:

```python
dict1 = {"a": 1}
dict2 = {"a": 99}

dict1.update(dict2)
print(dict1)  # {'a': 99}
```

### `.pop()`

Eliminar y devolver un valor:

```python
diccionario = {"a": 1, "b": 2}
valor = diccionario.pop("a")
print(valor)  # 1
print(diccionario)  # {'b': 2}
```

Con valor por defecto si no existe:

```python
valor = diccionario.pop("c", "no encontrado")
print(valor)  # no encontrado
```

### `.clear()`

Vaciar un diccionario:

```python
diccionario = {"a": 1, "b": 2}
diccionario.clear()
print(diccionario)  # {}
```

---

## 6. Comprensiones de Diccionarios

### Crear diccionarios con sintaxis concisa

**Patrón básico:**
```python
{clave: valor for elemento in iterable}
```

### Ejemplo 1: Duplicar valores

```python
original = {"a": 1, "b": 2, "c": 3}
duplicado = {k: v * 2 for k, v in original.items()}
print(duplicado)  # {'a': 2, 'b': 4, 'c': 6}
```

### Ejemplo 2: Filtrar

```python
numeros = {"a": 1, "b": 5, "c": 3}
mayores_que_2 = {k: v for k, v in numeros.items() if v > 2}
print(mayores_que_2)  # {'b': 5, 'c': 3}
```

### Ejemplo 3: Transformar claves y valores

```python
palabras = {"hola": 4, "mundo": 5}
resultado = {k.upper(): v for k, v in palabras.items()}
print(resultado)  # {'HOLA': 4, 'MUNDO': 5}
```

### Ejemplo 4: Crear desde listas

```python
claves = ["a", "b", "c"]
valores = [1, 2, 3]

diccionario = {k: v for k, v in zip(claves, valores)}
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3}
```

---

## 7. Debugging de Diccionarios

### Técnica 1: Impresión Formateada

```python
datos = {"nombre": "Miguel", "edad": 20, "ciudad": "Madrid"}

# Simple
print(datos)

# Mejor legibilidad
import json
print(json.dumps(datos, indent=2, ensure_ascii=False))
```

**Salida:**
```
{
  "nombre": "Miguel",
  "edad": 20,
  "ciudad": "Madrid"
}
```

### Técnica 2: Verificar estructura

```python
datos = {"usuario": {"nombre": "Miguel", "edad": 20}}

# Verificar existencia antes de acceder
if "usuario" in datos and "edad" in datos["usuario"]:
    print(datos["usuario"]["edad"])
else:
    print("Estructura incompleta")
```

### Técnica 3: Debugging paso a paso

```python
def procesar_diccionario(datos):
    print(f"[1] Datos iniciales: {datos}")
    
    resultado = {}
    for clave, valor in datos.items():
        print(f"[2] Procesando: {clave} = {valor}")
        resultado[clave] = valor * 2
        print(f"[3] Resultado parcial: {resultado}")
    
    return resultado

procesar_diccionario({"a": 1, "b": 2})
```

---

## 8. Ejercicios Progresivos

### Ejercicio 1: Acceso Seguro (Fácil)

**Objetivo:** Crear una función que acceda de forma segura a valores anidados.

```python
def obtener_valor_seguro(diccionario, clave1, clave2=None):
    """
    Obtiene un valor de un diccionario de forma segura.
    
    Ejemplo:
    datos = {"usuario": {"edad": 20}}
    obtener_valor_seguro(datos, "usuario", "edad")  # 20
    obtener_valor_seguro(datos, "usuario", "nombre")  # None
    """
    # TODO: Si clave2 es None, devuelve diccionario.get(clave1)
    # TODO: Si clave2 no es None, devuelve el valor anidado de forma segura
    # TODO: Si no existe, devuelve None
    pass

# Prueba:
datos = {"usuario": {"edad": 20, "ciudad": "Madrid"}}
print(obtener_valor_seguro(datos, "usuario", "edad"))  # 20
print(obtener_valor_seguro(datos, "usuario", "nombre"))  # None
print(obtener_valor_seguro(datos, "otros"))  # None
```

---

### Ejercicio 2: Transformación con Comprensión (Medio)

**Objetivo:** Transformar datos de una estructura a otra.

```python
def convertir_lista_a_diccionario(lista_de_tuplas):
    """
    Convierte una lista de tuplas en diccionario.
    
    Ejemplo:
    [("nombre", "Miguel"), ("edad", 20)] 
    →  {"nombre": "Miguel", "edad": 20}
    """
    # TODO: Usa comprensión de diccionarios
    pass

# Prueba:
datos = [("nombre", "Miguel"), ("edad", 20), ("ciudad", "Madrid")]
resultado = convertir_lista_a_diccionario(datos)
print(resultado)  # {'nombre': 'Miguel', 'edad': 20, 'ciudad': 'Madrid'}
```

---

### Ejercicio 3: Filtrar Diccionario (Medio)

**Objetivo:** Filtrar un diccionario según una condición.

```python
def filtrar_diccionario(diccionario, predicado):
    """
    Filtra un diccionario manteniendo solo los pares donde predicado es True.
    
    predicado: función que recibe (clave, valor) y devuelve True/False
    
    Ejemplo:
    datos = {"a": 1, "b": 5, "c": 3}
    filtrar_diccionario(datos, lambda k, v: v > 2)
    →  {'b': 5, 'c': 3}
    """
    # TODO: Usa comprensión de diccionarios
    # TODO: Llama a predicado(clave, valor) para cada par
    pass

# Prueba:
datos = {"a": 1, "b": 5, "c": 3, "d": 2}

# Valores mayores que 2
resultado1 = filtrar_diccionario(datos, lambda k, v: v > 2)
print(resultado1)  # {'b': 5, 'c': 3}

# Claves que contienen 'a'
resultado2 = filtrar_diccionario(datos, lambda k, v: 'a' in k)
print(resultado2)  # {'a': 1}
```

---

### Ejercicio 4: Fusionar y Deduplicar (Avanzado)

**Objetivo:** Fusionar dos diccionarios resolviendo conflictos.

```python
def fusionar_diccionarios(dict1, dict2, resolver_conflicto=None):
    """
    Fusiona dos diccionarios. Si hay claves duplicadas:
    - Si resolver_conflicto es None: dict2 sobrescribe dict1
    - Si resolver_conflicto es función: la función decide (recibe: clave, valor1, valor2)
    
    Ejemplo:
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 99, "c": 3}
    
    # Sin resolver: dict2 gana
    fusionar_diccionarios(dict1, dict2)
    →  {'a': 1, 'b': 99, 'c': 3}
    
    # Con resolver: toma el mayor
    fusionar_diccionarios(dict1, dict2, lambda k, v1, v2: max(v1, v2))
    →  {'a': 1, 'b': 99, 'c': 3}
    """
    # TODO: Crea un diccionario resultado
    # TODO: Copia dict1 al resultado
    # TODO: Para cada par en dict2:
    #       - Si no existe en resultado, agrégalo
    #       - Si existe y hay resolver_conflicto, usa resolver_conflicto
    #       - Si existe y no hay resolver_conflicto, sobrescribe con dict2
    pass

# Prueba 1: Sin resolver (default)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}
print(fusionar_diccionarios(dict1, dict2))
# {'a': 1, 'b': 99, 'c': 3}

# Prueba 2: Con resolver (toma el mayor)
print(fusionar_diccionarios(dict1, dict2, lambda k, v1, v2: max(v1, v2)))
# {'a': 1, 'b': 99, 'c': 3}

# Prueba 3: Con resolver (concatena strings)
dict1 = {"nombre": "Miguel", "apellido": "García"}
dict2 = {"nombre": " López", "ciudad": "Madrid"}
print(fusionar_diccionarios(dict1, dict2, lambda k, v1, v2: v1 + v2))
# {'nombre': 'Miguel López', 'apellido': 'García', 'ciudad': 'Madrid'}
```

---

### Ejercicio 5: Aplanar Diccionario Anidado (Avanzado)

**Objetivo:** Convertir un diccionario anidado en uno plano.

```python
def aplanar_diccionario(diccionario, prefijo=""):
    """
    Convierte un diccionario anidado en uno plano.
    
    Ejemplo:
    datos = {
        "usuario": {
            "nombre": "Miguel",
            "edad": 20
        },
        "ciudad": "Madrid"
    }
    
    aplanar_diccionario(datos)
    →  {
        'usuario_nombre': 'Miguel',
        'usuario_edad': 20,
        'ciudad': 'Madrid'
    }
    """
    # TODO: Itera sobre los items del diccionario
    # TODO: Si el valor es otro diccionario, llama recursivamente con prefijo
    # TODO: Si no, agrega al resultado con la clave formada
    pass

# Prueba:
datos = {
    "usuario": {
        "nombre": "Miguel",
        "edad": 20,
        "contacto": {
            "email": "miguel@example.com",
            "telefono": "123456"
        }
    },
    "ciudad": "Madrid"
}

resultado = aplanar_diccionario(datos)
print(resultado)
# {
#   'usuario_nombre': 'Miguel',
#   'usuario_edad': 20,
#   'usuario_contacto_email': 'miguel@example.com',
#   'usuario_contacto_telefono': '123456',
#   'ciudad': 'Madrid'
# }
```

---

## 9. `defaultdict` y `Counter` (Bonus)

### `defaultdict`: Evitar KeyError

```python
from collections import defaultdict

# Sin defaultdict: necesitas .get() o verificar
contador = {}
contador["a"] = contador.get("a", 0) + 1

# Con defaultdict: automático
contador = defaultdict(int)
contador["a"] += 1
contador["b"] += 1
print(contador)  # defaultdict(<class 'int'>, {'a': 1, 'b': 1})
```

### `Counter`: Contar elementos

```python
from collections import Counter

palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
frecuencia = Counter(palabras)

print(frecuencia)  # Counter({'hola': 3, 'mundo': 2, 'python': 1})
print(frecuencia.most_common(2))  # [('hola', 3), ('mundo', 2)]
```

---

## 10. Checklist de Comprensión

- [ ] Entiendo cómo acceder de forma segura a valores con `.get()`
- [ ] Puedo iterar sobre diccionarios con `.items()`
- [ ] Entiendo diccionarios anidados y cómo acceder a ellos
- [ ] Puedo usar comprensiones de diccionarios
- [ ] Puedo filtrar y transformar diccionarios
- [ ] Entiendo cómo debuggear diccionarios complejos
- [ ] Conozco `defaultdict` y `Counter`
- [ ] Puedo crear funciones que trabajen con diccionarios

---

## 11. Próximos Pasos

Una vez completes estos ejercicios:

1. Combina diccionarios con context managers: abre un JSON, procésalo, guárdalo
2. Explora `json.dumps()` y `json.loads()` para trabajar con JSON
3. Intenta procesar datos reales (CSV convertido a diccionarios)

**¿Dudas?**
1. Usa `print(diccionario)` o `json.dumps()` para ver la estructura
2. Verifica claves con `if clave in diccionario`
3. Usa debugger de PyCharm si necesitas inspeccionar paso a paso