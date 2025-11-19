# 🔄 Guía: Generadores en Python

## ¿Qué son los generadores?

Los generadores son funciones que **generan valores uno por uno, bajo demanda**, en lugar de crear una colección completa en memoria.

### El problema que resuelven

**Ejemplo:**
```python
# ❌ Lista tradicional - carga todo en memoria
def numeros_lista(n):
    resultado = []
    for i in range(n):
        resultado.append(i)
    return resultado

nums = numeros_lista(10_000_000)  # ¡10 millones de números en memoria!
```

**Con generador:**
```python
# ✅ Generador - genera uno por uno
def numeros_generador(n):
    for i in range(n):
        yield i

nums = numeros_generador(10_000_000)  # ¡Solo guarda el estado actual!
```

---

## Sintaxis básica: `yield`

La palabra clave `yield` convierte una función en generador:

```python
def contador(hasta):
    num = 1
    while num <= hasta:
        yield num  # Pausa aquí y devuelve el valor
        num += 1
```

---

## Características clave

### 1. Lazy Evaluation (Evaluación Perezosa)

El código **NO se ejecuta** hasta que pides valores:

```python
def ejemplo():
    print("Inicio")
    yield 1
    print("Medio")
    yield 2

gen = ejemplo()  # ¡NO imprime nada todavía!
```

### 2. Pausar y reanudar

El generador **recuerda** dónde se quedó:

```python
def ejemplo():
    print("Inicio")
    yield 1
    print("Medio")
    yield 2
    print("Fin")

gen = ejemplo()
print(next(gen))  # Imprime: "Inicio", devuelve 1, SE PAUSA
print(next(gen))  # Imprime: "Medio", devuelve 2, SE PAUSA
print(next(gen))  # Imprime: "Fin", lanza StopIteration
```

### 3. Memoria eficiente

Solo mantiene:
- El valor actual
- El estado de las variables locales
- La posición en el código

---

## Formas de usar generadores

### Opción 1: Bucle `for` (recomendado)

```python
def pares(n):
    for i in range(2, n + 1, 2):
        yield i

# El for llama automáticamente a next()
for numero in pares(10):
    print(numero)  # 2, 4, 6, 8, 10
```

### Opción 2: Función `next()` manual

```python
gen = pares(10)
print(next(gen))  # 2
print(next(gen))  # 4
print(next(gen))  # 6
# ...
```

### Opción 3: Convertir a lista

```python
gen = pares(10)
lista = list(gen)  # [2, 4, 6, 8, 10]
```

⚠️ **Cuidado:** Esto carga todo en memoria, perdiendo la ventaja del generador.

---

## Flujo de ejecución detallado

```python
def ejemplo():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")

# Paso 1: Crear generador
gen = ejemplo()
# Consola: (nada)

# Paso 2: Primera llamada a next()
valor1 = next(gen)
# Consola: "A"
# Retorna: 1
# Estado: PAUSADO después del primer yield

# Paso 3: Segunda llamada a next()
valor2 = next(gen)
# Consola: "B"
# Retorna: 2
# Estado: PAUSADO después del segundo yield

# Paso 4: Tercera llamada a next()
# Consola: "C"
# Lanza: StopIteration (no hay más yields)
```

---

## Casos de uso comunes

### 1. Leer archivos grandes

```python
def leer_lineas(archivo):
    with open(archivo, "r") as f:
        for linea in f:
            yield linea.strip()

# Procesa línea por línea sin cargar todo el archivo
for linea in leer_lineas("huge_file.txt"):
    procesar(linea)
```

### 2. Secuencias infinitas

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Genera Fibonacci infinitamente
for num in fibonacci():
    if num > 1000:
        break
    print(num)
```

### 3. Procesar datos en streaming

```python
def filtrar_pares(numeros):
    for num in numeros:
        if num % 2 == 0:
            yield num

def multiplicar(numeros, factor):
    for num in numeros:
        yield num * factor

# Pipeline de transformaciones
datos = range(100)
pares = filtrar_pares(datos)
resultado = multiplicar(pares, 10)

for valor in resultado:
    print(valor)  # 0, 20, 40, 60...
```

---

## Generadores vs Listas

| Aspecto | Lista | Generador |
|---------|-------|-----------|
| Memoria | Todo en memoria | Solo valor actual |
| Velocidad inicial | Lenta (crea todo) | Instantánea |
| Acceso | Aleatorio (`lista[5]`) | Secuencial |
| Reutilizable | Sí | No (se agota) |
| Tamaño | Finito | Puede ser infinito |

---

## Generator Expressions

Similar a list comprehensions, pero con paréntesis:

```python
# List comprehension (crea lista completa)
cuadrados_lista = [x**2 for x in range(1000)]

# Generator expression (genera bajo demanda)
cuadrados_gen = (x**2 for x in range(1000))

# Uso
for cuadrado in cuadrados_gen:
    print(cuadrado)
```

---

## Comparación con Java/Kotlin

**Kotlin Sequences:**
```kotlin
val numeros = sequence {
    yield(1)
    yield(2)
    yield(3)
}
```

**Python equivalente:**
```python
def numeros():
    yield 1
    yield 2
    yield 3
```

**Java Streams (conceptualmente similar):**
```java
Stream.iterate(1, n -> n + 1)
      .limit(10)
      .forEach(System.out::println);
```

**Python equivalente:**
```python
def contador(inicio, limite):
    for i in range(inicio, inicio + limite):
        yield i

for num in contador(1, 10):
    print(num)
```

---

## Errores comunes

### 1. Olvidar que se agotan

```python
gen = pares(10)
lista1 = list(gen)  # [2, 4, 6, 8, 10]
lista2 = list(gen)  # [] ← ¡Vacío! Ya se consumió
```

### 2. No capturar el generador

```python
pares(10)  # ❌ No hace nada

for num in pares(10):  # ✅ Correcto
    print(num)
```

### 3. Usar return en lugar de yield

```python
def incorrecto(n):
    return n  # ❌ Devuelve un valor y termina

def correcto(n):
    yield n  # ✅ Devuelve y pausa
```

---

## Cuándo usar generadores

✅ **Úsalos cuando:**
- Trabajas con archivos grandes
- Generas secuencias largas o infinitas
- Quieres procesar datos en pipeline
- La memoria es limitada
- No necesitas acceso aleatorio

❌ **No los uses cuando:**
- Necesitas acceso aleatorio a elementos
- Vas a iterar múltiples veces sobre los datos
- El dataset es pequeño (< 1000 elementos)
- Necesitas calcular `len()` o hacer slicing

---

## Resumen rápido

```python
# Crear generador
def mi_generador(n):
    for i in range(n):
        yield i

# Usar generador
for valor in mi_generador(5):
    print(valor)

# Características clave:
# 1. yield pausa la función
# 2. Lazy evaluation (no ejecuta hasta que pides valores)
# 3. Memoria eficiente (solo valor actual)
# 4. Se agotan después de usarlos
```

---

## Recursos adicionales

- [PEP 255 - Simple Generators](https://www.python.org/dev/peps/pep-0255/)
- [Python Docs - Generators](https://docs.python.org/3/howto/functional.html#generators)