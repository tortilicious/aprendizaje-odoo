# 🚀 Python Avanzado - Día 5: Decoradores & Virtualenv

> **Objetivo del Día:** Dominar decoradores (herramienta CRÍTICA para Odoo) y configurar tu entorno de trabajo.
> 
> **Importancia para Odoo:** ⭐⭐⭐⭐⭐ (CRÍTICO - Los usarás todos los días)

**Tiempo estimado:** 4-5 horas

---

## 📚 Índice Día 5

1. **Entender qué son los decoradores**
2. **Decoradores básicos**
3. **Decoradores con parámetros**
4. **Patrones de decoradores usados en Odoo**
5. **Virtualenv y gestión de dependencias**
6. **Ejercicios prácticos**
7. **Proyecto mini: Sistema de validación**

---

# 1️⃣ ¿QUÉ SON LOS DECORADORES?

## El Concepto Clave

Un **decorador es una función que modifica/envuelve otra función o clase sin cambiar su código original.**

### Analogía: Empapelar una Habitación

```
Habitación original = tu función
Papel tapiz = decorador

Habitación con papel tapiz = función decorada (misma, pero mejorada)
```

La habitación sigue siendo la misma, pero ahora tiene funcionalidades añadidas:
- Se ve mejor
- Mantiene más el calor
- Es más acogedora

**Las funciones funcionan igual, pero con comportamientos extra.**

## Ejemplo Visual

```python
# ❌ Sin decorador: función básica
def saludar(nombre):
    print(f"Hola {nombre}")

# Con decorador: misma función, pero con logging automático
@decorador_logging
def saludar(nombre):
    print(f"Hola {nombre}")

# Cuando llamas saludar("Ana"), automáticamente:
# 1. El decorador registra que se llamó
# 2. Ejecuta la función
# 3. Registra que terminó
```

---

# 2️⃣ DECORADORES BÁSICOS

## Estructura Fundamental

```python
def mi_decorador(func):
    """
    Un decorador es una función que recibe otra función
    y retorna una versión modificada
    """
    def wrapper(*args, **kwargs):
        # Código ANTES de ejecutar la función
        print(f"⏳ Antes de {func.__name__}")
        
        # Ejecutar la función original
        resultado = func(*args, **kwargs)
        
        # Código DESPUÉS de ejecutar la función
        print(f"✅ Después de {func.__name__}")
        
        return resultado
    
    return wrapper


# Aplicar decorador
@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")
    return f"Saludado a {nombre}"


# Uso
saludar("Ana")
```

**Output:**
```
⏳ Antes de saludar
Hola Ana
✅ Después de saludar
```

## Paso a Paso: Qué Sucede

```python
# 1️⃣ Python lee esto:
@mi_decorador
def saludar(nombre):
    pass

# 2️⃣ Python hace esto internamente:
def saludar(nombre):
    pass
saludar = mi_decorador(saludar)

# 3️⃣ Ahora saludar es en realidad wrapper()
# 4️⃣ Cuando llamas saludar("Ana"), llamas wrapper("Ana")
```

## *args y **kwargs: Aceptar Cualquier Parámetro

```python
def decorador_flexible(func):
    def wrapper(*args, **kwargs):
        # *args captura argumentos posicionales: (1, 2, 3)
        # **kwargs captura argumentos con nombre: {'a': 1, 'b': 2}
        print(f"Argumentos posicionales: {args}")
        print(f"Argumentos nombrados: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@decorador_flexible
def operacion(a, b, c=10):
    return a + b + c


operacion(5, 3)           # args=(5,3), kwargs={}
operacion(5, 3, c=20)     # args=(5,3), kwargs={'c': 20}
```

---

## 🎯 EJERCICIOS - DÍA 5 (Parte 1: Decoradores Básicos)

### Ejercicio 1: Decorador de Bienvenida

**Enunciado:**

Crea un decorador llamado `decorador_bienvenida` que:

1. ANTES de ejecutar la función, imprima: `"🎬 Iniciando [nombre_función]"`
2. Ejecute la función normalmente
3. DESPUÉS de ejecutar, imprima: `"🎬 Finalizado [nombre_función]"`
4. Retorne el resultado de la función

Prueba con una función `crear_usuario(nombre, email)` que retorne un diccionario `{'nombre': nombre, 'email': email}`.

**Resultado esperado al llamar `crear_usuario("Ana", "ana@email.com")`:**
```
🎬 Iniciando crear_usuario
🎬 Finalizado crear_usuario
{'nombre': 'Ana', 'email': 'ana@email.com'}
```

---

### Ejercicio 2: Decorador de Validación - Números Positivos

**Enunciado:**

Crea un decorador llamado `solo_positivos` que:

1. Verifique que TODOS los argumentos de la función sean números >= 0
2. Si alguno es negativo, lance `ValueError` con mensaje: `"❌ Número negativo detectado: [número]"`
3. Si todos son válidos, ejecute la función normalmente

Prueba con estas funciones:
- `calcular_area(ancho, alto)` - multiplica ancho * alto
- `calcular_precio_con_descuento(precio, descuento)` - resta descuento de precio

**Casos de prueba:**
```python
calcular_area(5, 10)      # ✅ Debe retornar 50
calcular_area(-5, 10)     # ❌ Debe lanzar ValueError
```

---

### Ejercicio 3: Decorador de Contador de Llamadas

**Enunciado:**

Crea un decorador llamado `contar_llamadas` que:

1. Cuente cuántas veces se ha llamado la función
2. Imprima ANTES de ejecutar: `"📞 Llamada #[número]"`
3. Ejecute la función
4. Retorne el resultado

**Pista:** Necesitarás usar una variable en el decorador para mantener el contador.

Prueba con una función `saludar(nombre)` que simplemente imprima `"Hola {nombre}"`.

**Resultado esperado:**
```python
saludar("Ana")    # Imprime: "📞 Llamada #1" + "Hola Ana"
saludar("Luis")   # Imprime: "📞 Llamada #2" + "Hola Luis"
saludar("Ana")    # Imprime: "📞 Llamada #3" + "Hola Ana"
```

---

# 3️⃣ DECORADORES CON PARÁMETROS

## Nivel 2: Decorador que Recibe Parámetros

Este es el patrón que **Odoo usa constantemente**.

```python
def decorador_con_parametros(mensaje):
    """
    Decorador que recibe parámetros.
    
    Estructura:
    1. Función externa: recibe los parámetros
    2. Función decorador: recibe la función a decorar
    3. Función wrapper: ejecuta la lógica
    """
    def decorador_real(func):
        def wrapper(*args, **kwargs):
            print(f"📝 {mensaje}")
            resultado = func(*args, **kwargs)
            print(f"✅ Completado")
            return resultado
        return wrapper
    return decorador_real


# Uso
@decorador_con_parametros("Procesando pago...")
def procesar_pago(cantidad):
    print(f"Pagando {cantidad}€")
    return True
```

**Output:**
```
📝 Procesando pago...
Pagando 100€
✅ Completado
```

## Cómo Funciona Internamente

```python
# Esto:
@decorador_con_parametros("Mi mensaje")
def mi_funcion():
    pass

# Es equivalente a:
def mi_funcion():
    pass
mi_funcion = decorador_con_parametros("Mi mensaje")(mi_funcion)

# Paso a paso:
# 1. decorador_con_parametros("Mi mensaje") retorna decorador_real
# 2. decorador_real(mi_funcion) retorna wrapper
# 3. mi_funcion ahora es wrapper
```

## Patrones en Odoo

```python
# En Odoo verás patrones como estos:

@api.depends('campo1', 'campo2')  # <- parámetros
def _compute_total(self):         # <- función
    pass

@api.onchange('precio', 'cantidad')  # <- parámetros
def _onchange_total(self):           # <- función
    pass

@api.constrains('email')  # <- parámetros
def _check_email(self):   # <- función
    pass
```

---

## 🎯 EJERCICIOS - DÍA 5 (Parte 2: Decoradores con Parámetros)

### Ejercicio 4: Decorador de Validación Personalizable

**Enunciado:**

Crea un decorador llamado `validar_rango` que acepte dos parámetros: `minimo` y `maximo`.

El decorador debe:

1. Validar que el RESULTADO de la función esté en el rango [minimo, maximo]
2. Si está fuera del rango, lanzar `ValueError` con mensaje: `"❌ Resultado {resultado} fuera de rango [{minimo}, {maximo}]"`
3. Si está dentro, retornar el resultado normalmente

Prueba con estas funciones:
- `calcular_descuento(precio, porcentaje)` - debe retornar entre 0 y 100 (porcentaje)
- `calcular_edad(anio_nacimiento)` - debe retornar entre 0 y 130 (edad)

**Casos de prueba:**
```python
@validar_rango(0, 100)
def calcular_descuento(precio):
    return precio * 0.5  # Si precio=100, retorna 50 ✅

@validar_rango(0, 100)
def calcular_descuento(precio):
    return precio * 1.5  # Si precio=100, retorna 150 ❌ ERROR
```

---

### Ejercicio 5: Decorador de Reintentos (Patrón Importante)

**Enunciado:**

Crea un decorador llamado `reintentar` que acepte:
- `max_intentos` (número máximo de reintentos)
- `espera` (segundos a esperar entre intentos, default=1)

El decorador debe:

1. Intentar ejecutar la función
2. Si falla (lanza excepción), reintentar hasta `max_intentos` veces
3. Esperar `espera` segundos entre intentos
4. Imprimir mensaje en cada intento: `"Intento [n]/[max_intentos]"`
5. Si llega al máximo y sigue fallando, relanzar la excepción

**Pista:** Necesitarás `time.sleep(espera)` entre reintentos.

Prueba con una función que a veces falla:
```python
@reintentar(max_intentos=3, espera=0.5)
def conectar_a_servidor():
    import random
    if random.random() < 0.7:  # 70% de fallar
        raise ConnectionError("Servidor no responde")
    return "Conectado ✅"
```

---

### Ejercicio 6: Decorador de Caché Simple

**Enunciado:**

Crea un decorador llamado `con_cache` que:

1. Almacene los resultados de llamadas anteriores
2. Si se llama con los mismos argumentos, retorne el resultado cacheado sin ejecutar
3. Imprima cuando usa caché: `"💾 Resultado en caché"`
4. Imprima cuando calcula: `"🔄 Calculando..."`

Prueba con esta función:
```python
@con_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)  # Primera vez: "🔄 Calculando..." (lento)
fibonacci(10)  # Segunda vez: "💾 Resultado en caché" (instant)
```

---

# 4️⃣ USAR `functools.wraps` - Buena Práctica

Cuando creas decoradores, **siempre usa `functools.wraps`** para preservar metadatos:

```python
from functools import wraps

def mi_decorador(func):
    @wraps(func)  # ← IMPORTANTE: preserva información de la función original
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Después")
        return resultado
    return wrapper

@mi_decorador
def mi_funcion():
    """Esto es mi función"""
    pass

# Sin @wraps, mi_funcion.__doc__ sería "Esto es mi función"
# Pero sin @wraps, sería None
print(mi_funcion.__doc__)  # "Esto es mi función" ✅
print(mi_funcion.__name__) # "mi_funcion" ✅
```

---

# 5️⃣ VIRTUALENV Y GESTIÓN DE DEPENDENCIAS

## ¿Por qué Virtualenv?

Cada proyecto Python tiene sus propias dependencias con versiones específicas.

```
Proyecto A: Django 4.0 + Python 3.9
Proyecto B: Django 5.0 + Python 3.11

Sin virtualenv: CONFLICTO ❌
Con virtualenv: AISLADO ✅
```

## Workflow Paso a Paso

### 1. Crear entorno virtual

```bash
python -m venv venv_proyecto
```

Esto crea una carpeta `venv_proyecto` con Python aislado.

### 2. Activar el entorno

**Linux/macOS:**
```bash
source venv_proyecto/bin/activate
```

**Windows:**
```bash
venv_proyecto\Scripts\activate
```

**Indicador:** Verás `(venv_proyecto)` al inicio de la terminal.

### 3. Instalar dependencias

```bash
pip install odoo requests
```

### 4. Guardar dependencias

```bash
pip freeze > requirements.txt
```

Genera archivo como:
```txt
odoo==17.0
psycopg2-binary==2.9.9
requests==2.31.0
```

### 5. Otra persona instala igual

```bash
pip install -r requirements.txt
```

### 6. Desactivar

```bash
deactivate
```

---

## 🎯 EJERCICIOS - DÍA 5 (Parte 3: Virtualenv)

### Ejercicio 7: Configurar Virtualenv para tu Proyecto

**Enunciado:**

Sigue estos pasos EN TU TERMINAL (no en código):

1. Crea una carpeta nueva: `python_avanzado_dia5`
2. Entra a la carpeta
3. Crea un virtualenv llamado `venv`
4. **Activa** el virtualenv
5. Instala un paquete: `pip install requests`
6. Verifica que está instalado: `pip list` (debe aparecer requests)
7. Genera `requirements.txt`
8. Desactiva el virtualenv
9. Verifica que `requests` NO está disponible fuera del virtualenv

**Comando de verificación:**
```bash
# DENTRO del virtualenv (después de pip install requests)
python -c "import requests; print('✅ requests disponible')"

# FUERA del virtualenv (después de deactivate)
python -c "import requests; print('✅ requests disponible')"  # ❌ ERROR
```

---

### Ejercicio 8: Crear requirements.txt para Proyecto Odoo

**Enunciado:**

1. Crea un nuevo virtualenv
2. Actívalo
3. Instala estas dependencias (típicas para desarrollo Odoo):
   ```bash
   pip install odoo==17.0
   pip install psycopg2-binary
   pip install requests
   pip install python-dateutil
   ```
4. Genera `requirements.txt`
5. Mira el contenido del archivo
6. **Bonus:** Desactiva, elimina la carpeta venv, crea uno nuevo, e instala desde `requirements.txt`. Verifica que funciona.

**Resultado esperado:** `requirements.txt` con todas las dependencias y sus versiones exactas.

---

# 📋 RESUMEN DÍA 5

| Concepto | Qué es | Para qué sirve | Importancia |
|----------|--------|-----------------|-------------|
| **Decorador** | Función que modifica otra función | Añadir funcionalidades sin cambiar el código | ⭐⭐⭐⭐⭐ |
| **Decorador básico** | `@decorator` sin parámetros | Logging, validación simple | ⭐⭐⭐⭐ |
| **Decorador con parámetros** | `@decorator(param)` | Validaciones complejas, configurables | ⭐⭐⭐⭐⭐ |
| **@wraps** | Preserva metadatos de función | Buena práctica en decoradores | ⭐⭐⭐ |
| **Virtualenv** | Aislamiento de dependencias Python | Cada proyecto con sus versiones | ⭐⭐⭐⭐ |
| **pip freeze** | Captura versiones instaladas | Reproducibilidad en otros equipos | ⭐⭐⭐⭐ |

---

# 📝 CHECKLIST DÍA 5

- [ ] Entiendo qué es un decorador y cómo funciona
- [ ] Puedo crear un decorador básico con `@`
- [ ] Puedo crear un decorador que reciba parámetros
- [ ] Sé usar `@wraps` para preservar metadatos
- [ ] Puedo crear y activar un virtualenv
- [ ] Sé instalar, guardar y reproducir dependencias
- [ ] He completado los 8 ejercicios

---

# 🚀 Próximo Paso

**Día 6:** Generadores, Context Managers y Manejo Avanzado de Diccionarios

Prepárate para:
- Procesamiento eficiente de datos grandes
- Gestión automática de recursos
- Manipulación avanzada de diccionarios (crítico para Odoo)

---

*Apuntes Día 5 completados. Tiempo de estudio: 4-5 horas. ¡Mucho éxito! 🎯*