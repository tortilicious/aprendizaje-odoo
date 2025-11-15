# Context Managers en Python

## 1. Conceptos Fundamentales

### ¿Qué es un Context Manager?

Un context manager es un patrón que asegura que ciertos recursos se *inicialicen* antes de usarlos y se *limpien* después, **sin importar si hay error o no**.

**Analogía con Java:**
```java
// Java: try-with-resources
try (FileReader reader = new FileReader("archivo.txt")) {
    // usas reader
} // se cierra automáticamente
```

**Python: with**
```python
# Python: context manager
with open("archivo.txt") as f:
    # usas f
# se cierra automáticamente
```

### ¿Por qué los necesitamos?

Imagina este código sin context manager:
```python
f = open("archivo.txt")
# Si ocurre un error AQUÍ...
contenido = f.read()
f.close()  # Esto nunca se ejecuta, archivo queda abierto
```

Con context manager:
```python
with open("archivo.txt") as f:
    contenido = f.read()
# El archivo se cierra SIEMPRE, incluso si hay error
```

---

## 2. Anatomía de un Context Manager

### Los Dos Métodos Mágicos

Todo context manager tiene dos métodos especiales:

```python
class MiContextManager:
    def __enter__(self):
        """Se ejecuta al ENTRAR en el bloque 'with'"""
        print("Inicializando recurso...")
        return self  # Lo que devuelves aquí es lo que asignas en 'as'
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Se ejecuta al SALIR del bloque 'with' (siempre)"""
        print("Limpiando recurso...")
        return False  # False = propagar excepciones, True = silenciarlas
```

**¿Cómo se usa?**
```python
with MiContextManager() as cm:
    print("Dentro del bloque")
```

**Salida esperada:**
```
Inicializando recurso...
Dentro del bloque
Limpiando recurso...
```

### Parámetros de `__exit__`

Cuando ocurre una excepción dentro del bloque `with`, `__exit__` recibe información sobre ella:

- `exc_type`: Tipo de excepción (ej: `ValueError`)
- `exc_val`: La excepción en sí
- `exc_tb`: El traceback

**Ejemplo:**
```python
class ContextConControl:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Ocurrió error: {exc_type.__name__}: {exc_val}")
        return False  # Propagar el error
```

---

## 3. Tu Primer Context Manager

### Ejemplo 1: Archivo con Logging

```python
class ArchivoConLog:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = None
    
    def __enter__(self):
        print(f"📂 Abriendo {self.nombre}")
        self.archivo = open(self.nombre, 'r')
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"📂 Cerrando {self.nombre}")
        if self.archivo:
            self.archivo.close()
        return False
```

**Uso:**
```python
with ArchivoConLog("datos.txt") as f:
    contenido = f.read()
    print(contenido)
```

---

## 4. Debugging: Ver el Flujo de Ejecución

### Técnica 1: Print Debugging

Agrega `print()` en cada paso para ver el flujo:

```python
class DebugContext:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print(f"[ENTER] {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[EXIT] {self.nombre}")
        print(f"  exc_type: {exc_type}")
        print(f"  exc_val: {exc_val}")
        return False

# Prueba sin error
print("=== SIN ERROR ===")
with DebugContext("mi_cm") as cm:
    print("[DENTRO] Ejecutando código")

# Prueba con error
print("\n=== CON ERROR ===")
try:
    with DebugContext("mi_cm") as cm:
        print("[DENTRO] Ejecutando código")
        raise ValueError("Algo salió mal")
except ValueError:
    print("[CAPTURADO] Error manejado")
```

**Salida esperada:**
```
=== SIN ERROR ===
[ENTER] mi_cm
[DENTRO] Ejecutando código
[EXIT] mi_cm
  exc_type: None
  exc_val: None

=== CON ERROR ===
[ENTER] mi_cm
[DENTRO] Ejecutando código
[EXIT] mi_cm
  exc_type: <class 'ValueError'>
  exc_val: Algo salió mal
[CAPTURADO] Error manejado
```

### Técnica 2: PyCharm Debugger

1. Coloca breakpoints en `__enter__` y `__exit__`
2. Ejecuta en modo debug
3. Observa el stack de llamadas
4. Paso a paso (F10 = step over)

---

## 5. Ejercicios Progresivos

### Ejercicio 1: Context Manager Simple (Fácil)

**Objetivo:** Crear un context manager que mida tiempo de ejecución.

```python
import time

class Cronometro:
    def __enter__(self):
        # TODO: Guarda el tiempo de inicio
        # TODO: Devuelve self
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Calcula tiempo transcurrido
        # TODO: Imprime el resultado
        return False

# Prueba:
with Cronometro():
    time.sleep(2)
    print("Trabajando...")

# Salida esperada (aproximada):
# Trabajando...
# ⏱️ Tiempo: 2.001 segundos
```

**Pistas:**
- Usa `time.time()` para obtener el tiempo actual
- En `__enter__`, guarda el tiempo inicial en `self`
- En `__exit__`, calcula la diferencia

---

### Ejercicio 2: Context Manager con Archivo (Medio)

**Objetivo:** Crear un context manager que abra un archivo con encoding específico y maneje errores.

```python
class ArchivoSeguro:
    def __init__(self, ruta, encoding='utf-8'):
        self.ruta = ruta
        self.encoding = encoding
        self.archivo = None
    
    def __enter__(self):
        # TODO: Intenta abrir el archivo
        # TODO: Si no existe, imprime mensaje y devuelve None
        # TODO: Si existe, imprime que se abrió y devuelve el archivo
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Si el archivo está abierto, ciérralo
        # TODO: Si hubo excepción, imprime el tipo
        return False

# Prueba 1: archivo que existe
with ArchivoSeguro("existe.txt") as f:
    if f:
        print("Contenido:", f.read())

# Prueba 2: archivo que no existe
with ArchivoSeguro("no_existe.txt") as f:
    if f is None:
        print("Archivo no disponible")

# Prueba 3: error dentro del bloque
try:
    with ArchivoSeguro("existe.txt") as f:
        if f:
            numero = int(f.read())  # Error si no es número
except ValueError:
    print("Error capturado correctamente")
```

---

### Ejercicio 3: Context Manager con Control de Excepciones (Avanzado)

**Objetivo:** Crear un context manager que pueda silenciar excepciones específicas.

```python
class SuppressError:
    def __init__(self, *excepciones_a_ignorar):
        self.excepciones = excepciones_a_ignorar
    
    def __enter__(self):
        # TODO: Devuelve self
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Si exc_type es None, devuelve False
        # TODO: Si exc_type está en self.excepciones, devuelve True (silencia)
        # TODO: Si exc_type NO está en self.excepciones, devuelve False (propaga)
        pass

# Prueba 1: error ignorado
with SuppressError(ValueError):
    print("Antes del error")
    raise ValueError("Este error será silenciado")
    print("Después del error (no se ejecuta)")

print("Continuamos después del context manager")

# Prueba 2: error NO ignorado
try:
    with SuppressError(ValueError):
        raise KeyError("Este error NO será silenciado")
except KeyError:
    print("Error propagado correctamente")
```

---

## 6. La Forma Pythonica: Decorador `@contextmanager`

Python ofrece una forma más simple usando decoradores y generadores:

```python
from contextlib import contextmanager

@contextmanager
def mi_context():
    print("Inicializando")
    yield  # Lo que viene ANTES es __enter__
    print("Limpiando")  # Lo que viene DESPUÉS es __exit__

# Uso:
with mi_context():
    print("Dentro del bloque")
```

**Comparación:**

```python
# Forma 1: Clase con __enter__ y __exit__
class MiContext:
    def __enter__(self):
        print("Inicializando")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Limpiando")
        return False

# Forma 2: Decorador @contextmanager
@contextmanager
def mi_context():
    print("Inicializando")
    yield
    print("Limpiando")
```

---

## 7. Ejercicios con `@contextmanager`

### Ejercicio 4: Cronometro con Decorador

```python
from contextlib import contextmanager
import time

@contextmanager
def cronometro(nombre="operación"):
    # TODO: Implementa usando yield
    # Antes de yield: inicia tiempo
    # Después de yield: calcula y imprime tiempo
    pass

# Prueba:
with cronometro("descarga"):
    time.sleep(1)
    print("Descargando...")
```

---

### Ejercicio 5: Gestor de Cambio de Directorio

```python
from contextlib import contextmanager
import os

@contextmanager
def cambiar_directorio(ruta):
    # TODO: Guarda el directorio actual
    # TODO: Cambia al nuevo directorio
    # TODO: Yield
    # TODO: Vuelve al directorio original (en el finally implícito)
    pass

# Prueba:
print("Directorio actual:", os.getcwd())
with cambiar_directorio("/tmp"):
    print("Directorio temporal:", os.getcwd())
print("Volvimos a:", os.getcwd())
```

---

## 8. Debugging de Context Managers con `@contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def debug_context(nombre):
    print(f"[BEFORE YIELD] Entrando en {nombre}")
    try:
        yield
    except Exception as e:
        print(f"[EXCEPTION] {e}")
        raise
    finally:
        print(f"[FINALLY] Limpiando {nombre}")

# Prueba:
with debug_context("mi_operacion"):
    print("Ejecutando...")
```

---

## 9. Checklist de Comprensión

- [ ] Entiendo por qué existen los context managers (resource management)
- [ ] Puedo explicar qué es `__enter__` y `__exit__`
- [ ] Entiendo cómo se comportan las excepciones en `__exit__`
- [ ] Puedo crear un context manager simple con una clase
- [ ] Puedo debuggear un context manager viendo el flujo de ejecución
- [ ] Entiendo la diferencia entre `return False` y `return True` en `__exit__`
- [ ] Puedo crear un context manager con `@contextmanager`
- [ ] Puedo usar context managers reales como `open()` con confianza

---

## 10. Próximos Pasos

Una vez completes estos ejercicios:

1. Intenta crear un context manager que combine **dos recursos** (ej: archivo + conexión a BD)
2. Experimenta con `try/finally` dentro de `__exit__` para manejo robusto de errores
3. Explora `contextlib.closing()` y `contextlib.suppress()` en la documentación oficial

**¿Dudas? Estrategia:**
1. Lee el error completo
2. Usa `print()` para ver dónde falla
3. Coloca breakpoints en PyCharm si los prints no son suficientes