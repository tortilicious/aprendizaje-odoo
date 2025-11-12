# 📂 Guía: Trabajar con Archivos en Python

## Comparación Java vs Python

### 1. Abrir un archivo

**Java:**
```java
FileReader fr = new FileReader("datos.txt");
BufferedReader br = new BufferedReader(fr);
```

**Python:**
```python
archivo = open("datos.txt", "r")  # "r" = read (lectura)
```

**Modos comunes:**
- `"r"` - Lectura (read)
- `"w"` - Escritura (write) - sobrescribe el archivo
- `"a"` - Añadir (append) - añade al final
- `"r+"` - Lectura y escritura

---

### 2. Leer contenido

Python tiene **3 métodos principales:**

```python
archivo = open("datos.txt", "r")

# Opción 1: Leer TODO el archivo como string
contenido = archivo.read()
print(contenido)  # "Línea 1\nLínea 2\nLínea 3"

# Opción 2: Leer línea por línea en una lista
lineas = archivo.readlines()
print(lineas)  # ["Línea 1\n", "Línea 2\n", "Línea 3"]

# Opción 3: Iterar línea por línea (¡como generador!)
for linea in archivo:
    print(linea)  # "Línea 1\n", "Línea 2\n", etc.
```

---

### 3. Cerrar el archivo

**Java:**
```java
br.close();
fr.close();
```

**Python:**
```python
archivo.close()
```

⚠️ **PROBLEMA:** Si hay un error antes del `close()`, el archivo queda abierto.

---

### 4. El `with` statement - La forma correcta ✅

**Java (try-with-resources):**
```java
try (BufferedReader br = new BufferedReader(new FileReader("datos.txt"))) {
    // usar br
} // Se cierra automáticamente
```

**Python (with statement):**
```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
# El archivo se cierra AUTOMÁTICAMENTE aquí, incluso si hay error
```

El `with` garantiza que el archivo se cierre siempre, incluso si hay excepciones.

---

### 5. Eliminar saltos de línea

Cuando lees líneas, vienen con `\n` al final:

```python
linea = "Hola mundo\n"

# Opción 1: strip() - elimina espacios y \n de ambos lados
limpia = linea.strip()  # "Hola mundo"

# Opción 2: rstrip() - solo elimina del lado derecho
limpia = linea.rstrip()  # "Hola mundo"

# Opción 3: lstrip() - solo elimina del lado izquierdo
limpia = linea.lstrip()  # "Hola mundo\n"
```

---

## 📝 Ejemplo completo

```python
# Leer archivo línea por línea (mejor práctica)
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        print(linea_limpia)
```

---

## 💾 Escribir en archivos

```python
# Escribir (sobrescribe el archivo)
with open("salida.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")

# Añadir al final (no sobrescribe)
with open("salida.txt", "a") as archivo:
    archivo.write("Tercera línea\n")
```

---

## ⚠️ Manejo de errores

```python
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
except IOError:
    print("Error al leer el archivo")
```

---

## 🎯 Puntos clave a recordar

1. **Siempre usa `with`** para abrir archivos - garantiza el cierre automático
2. **Iterar línea por línea** es más eficiente que `read()` para archivos grandes
3. **`strip()`** elimina espacios y saltos de línea
4. El objeto archivo es **iterable** - puedes usarlo directamente en un `for`
5. Los modos `"r"`, `"w"`, `"a"` son los más comunes

---

## 📚 Referencia rápida

| Operación | Código |
|-----------|--------|
| Abrir para leer | `open("file.txt", "r")` |
| Abrir para escribir | `open("file.txt", "w")` |
| Abrir para añadir | `open("file.txt", "a")` |
| Leer todo | `archivo.read()` |
| Leer líneas | `archivo.readlines()` |
| Iterar líneas | `for linea in archivo:` |
| Escribir | `archivo.write("texto")` |
| Cerrar | `archivo.close()` (mejor usar `with`) |