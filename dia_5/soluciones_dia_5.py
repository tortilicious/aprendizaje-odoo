# ✅ SOLUCIONES COMENTADAS - DÍA 5: DECORADORES & VIRTUALENV
# ============================================================

"""
IMPORTANTE: 
- Estas son SOLUCIONES COMENTADAS
- Pueden haber otras formas correctas de resolver estos ejercicios
- Lo importante es que ENTIENDAS la lógica
- No memorices, entiende y practica
"""

# =============================================================================
# EJERCICIO 1: Decorador de Bienvenida
# =============================================================================

from functools import wraps

def decorador_bienvenida(func):
    """
    Decorador que registra entrada y salida de función.
    
    Estructura típica:
    1. Función decoradora (recibe la función a decorar)
    2. Función wrapper (la que realmente se ejecuta)
    3. Retorna wrapper
    """
    @wraps(func)  # ← Preserva metadatos de la función original
    def wrapper(*args, **kwargs):
        # ANTES de ejecutar
        print(f"🎬 Iniciando {func.__name__}")
        
        # Ejecutar la función original
        resultado = func(*args, **kwargs)
        
        # DESPUÉS de ejecutar
        print(f"🎬 Finalizado {func.__name__}")
        
        # Retornar el resultado
        return resultado
    
    return wrapper


# Prueba
@decorador_bienvenida
def crear_usuario(nombre, email):
    """Crea un usuario y retorna sus datos"""
    return {'nombre': nombre, 'email': email}


# Ejecución
print("--- Ejercicio 1 ---")
resultado = crear_usuario("Ana", "ana@email.com")
print(resultado)

# Output esperado:
# 🎬 Iniciando crear_usuario
# 🎬 Finalizado crear_usuario
# {'nombre': 'Ana', 'email': 'ana@email.com'}


# =============================================================================
# EJERCICIO 2: Decorador de Validación - Números Positivos
# =============================================================================

def solo_positivos(func):
    """
    Decorador que valida que TODOS los argumentos sean números >= 0.
    
    Estrategia:
    1. Capturar todos los argumentos (*args, **kwargs)
    2. Validar que sean números y positivos
    3. Si alguno falla, lanzar ValueError
    4. Si todo está bien, ejecutar la función
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Validar argumentos posicionales
        for arg in args:
            # Verificar que es número (int o float)
            if not isinstance(arg, (int, float)):
                raise ValueError(f"❌ Argumento no es número: {arg}")
            
            # Verificar que es positivo (>= 0)
            if arg < 0:
                raise ValueError(f"❌ Número negativo detectado: {arg}")
        
        # Validar argumentos con nombre
        for clave, valor in kwargs.items():
            if not isinstance(valor, (int, float)):
                raise ValueError(f"❌ Argumento {clave} no es número: {valor}")
            if valor < 0:
                raise ValueError(f"❌ Número negativo detectado: {valor}")
        
        # Si todo es válido, ejecutar
        return func(*args, **kwargs)
    
    return wrapper


# Prueba
@solo_positivos
def calcular_area(ancho, alto):
    """Calcula el área de un rectángulo"""
    return ancho * alto


@solo_positivos
def calcular_precio_con_descuento(precio, descuento):
    """Calcula precio después de aplicar descuento"""
    return precio - descuento


print("\n--- Ejercicio 2 ---")

# Caso válido
try:
    print(f"Área: {calcular_area(5, 10)}")  # ✅ 50
except ValueError as e:
    print(f"Error: {e}")

# Caso con número negativo
try:
    print(f"Área: {calcular_area(-5, 10)}")  # ❌
except ValueError as e:
    print(f"Error: {e}")

# Caso con precio y descuento válidos
try:
    print(f"Precio final: {calcular_precio_con_descuento(100, 20)}")  # ✅ 80
except ValueError as e:
    print(f"Error: {e}")


# =============================================================================
# EJERCICIO 3: Decorador de Contador de Llamadas
# =============================================================================

def contar_llamadas(func):
    """
    Decorador que cuenta cuántas veces se ha llamado la función.
    
    Clave: Usar variable en el scope del decorador (closure)
    """
    contador = 0  # ← Variable que persiste entre llamadas
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal contador  # ← Permite modificar variable del scope exterior
        contador += 1
        
        print(f"📞 Llamada #{contador}")
        
        # Ejecutar función original
        return func(*args, **kwargs)
    
    return wrapper


# Prueba
@contar_llamadas
def saludar(nombre):
    """Saluda a una persona"""
    print(f"Hola {nombre}")


print("\n--- Ejercicio 3 ---")
saludar("Ana")     # Llamada #1
saludar("Luis")    # Llamada #2
saludar("Ana")     # Llamada #3

# Output:
# 📞 Llamada #1
# Hola Ana
# 📞 Llamada #2
# Hola Luis
# 📞 Llamada #3
# Hola Ana


# =============================================================================
# EJERCICIO 4: Decorador de Validación Personalizable
# =============================================================================

def validar_rango(minimo, maximo):
    """
    Decorador con parámetros que valida el RESULTADO de la función.
    
    Estructura de 3 niveles:
    1. Función externa: recibe los parámetros (minimo, maximo)
    2. Función decorador: recibe la función a decorar
    3. Función wrapper: ejecuta la lógica
    """
    def decorador_real(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Ejecutar la función
            resultado = func(*args, **kwargs)
            
            # Validar que el resultado esté en el rango
            if not (minimo <= resultado <= maximo):
                raise ValueError(
                    f"❌ Resultado {resultado} fuera de rango [{minimo}, {maximo}]"
                )
            
            return resultado
        
        return wrapper
    
    return decorador_real


# Prueba
@validar_rango(0, 100)
def calcular_descuento(precio):
    """Descuento debe estar entre 0 y 100%"""
    return precio * 0.5


print("\n--- Ejercicio 4 ---")

try:
    print(f"Descuento: {calcular_descuento(100)}")  # ✅ 50 (válido)
except ValueError as e:
    print(f"Error: {e}")

try:
    print(f"Descuento: {calcular_descuento(300)}")  # ❌ 150 (fuera de rango)
except ValueError as e:
    print(f"Error: {e}")


# =============================================================================
# EJERCICIO 5: Decorador de Reintentos
# =============================================================================

import time

def reintentar(max_intentos=3, espera=1):
    """
    Decorador que reintenta ejecutar una función si falla.
    
    Patrón importante:
    - Muy usado en conexiones a BD/servidores
    - Espera entre reintentos para que se recupere el servicio
    """
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Bucle de reintentos
            for intento in range(1, max_intentos + 1):
                try:
                    print(f"Intento {intento}/{max_intentos}")
                    
                    # Intentar ejecutar
                    return func(*args, **kwargs)
                
                except Exception as e:
                    # Si es el último intento, relanzar la excepción
                    if intento == max_intentos:
                        print(f"❌ Falló definitivamente: {e}")
                        raise
                    
                    # Si no es el último, esperar y reintentar
                    print(f"⚠️ Intento {intento} falló: {e}. Reintentando en {espera}s...")
                    time.sleep(espera)
        
        return wrapper
    
    return decorador


# Prueba
import random

@reintentar(max_intentos=3, espera=0.5)
def conectar_a_servidor():
    """Simula conexión que a veces falla"""
    # 70% de probabilidad de fallar
    if random.random() < 0.7:
        raise ConnectionError("Servidor no disponible")
    return "Conectado ✅"


print("\n--- Ejercicio 5 ---")
try:
    print(conectar_a_servidor())
except ConnectionError:
    print("No se pudo conectar después de 3 intentos")


# =============================================================================
# EJERCICIO 6: Decorador de Caché Simple
# =============================================================================

def con_cache(func):
    """
    Decorador que cachea (memoriza) resultados.
    
    Optimización importante:
    - Primera vez que llamas con args (5,): calcula y guarda
    - Segunda vez que llamas con args (5,): retorna del caché
    """
    cache = {}  # ← Diccionario que persiste entre llamadas
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Crear clave única del cache
        # (args es tupla, kwargs.items() es lista de tuplas)
        clave = (args, tuple(sorted(kwargs.items())))
        
        # Si está en cache, retornar directamente
        if clave in cache:
            print(f"💾 Resultado en caché para {args}")
            return cache[clave]
        
        # Si no, calcular
        print(f"🔄 Calculando para {args}")
        resultado = func(*args, **kwargs)
        
        # Guardar en cache
        cache[clave] = resultado
        
        return resultado
    
    return wrapper


# Prueba
@con_cache
def fibonacci(n):
    """Calcula fibonacci de forma recursiva (sin optimización, solo para demo)"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print("\n--- Ejercicio 6 ---")
print(f"Fib(5): {fibonacci(5)}")      # 🔄 Calcula (lento)
print(f"Fib(5): {fibonacci(5)}")      # 💾 Caché (instantáneo)
print(f"Fib(3): {fibonacci(3)}")      # 💾 Caché (ya se calculó como subproblema)


# =============================================================================
# EJERCICIO 7: Virtualenv (EN TERMINAL, NO EN CÓDIGO)
# =============================================================================

"""
EJERCICIO 7: PASOS EN TERMINAL (no es código Python)

1. Crear carpeta y entrar:
   mkdir python_avanzado_dia5
   cd python_avanzado_dia5

2. Crear virtualenv:
   python -m venv venv

3. Activar:
   # Linux/macOS:
   source venv/bin/activate
   
   # Windows:
   venv\Scripts\activate
   
   # Deberías ver: (venv) al inicio de la terminal

4. Instalar paquete:
   pip install requests

5. Verificar que está instalado:
   pip list
   
   Deberías ver: requests en la lista

6. Generar requirements.txt:
   pip freeze > requirements.txt

7. Ver el archivo:
   cat requirements.txt  # Linux/macOS
   type requirements.txt # Windows

8. Desactivar:
   deactivate

9. Verificar que NO está disponible:
   python -c "import requests; print('OK')"
   
   Deberías ver: ModuleNotFoundError

10. Bonus - Reinstalar desde requirements.txt:
    python -m venv venv2
    source venv2/bin/activate
    pip install -r requirements.txt
    python -c "import requests; print('OK')"  # Debe funcionar
"""


# =============================================================================
# EJERCICIO 8: Virtualenv para Odoo (EN TERMINAL)
# =============================================================================

"""
EJERCICIO 8: PASOS EN TERMINAL

1. Crear y activar nuevo virtualenv:
   mkdir odoo_dev
   cd odoo_dev
   python -m venv venv
   source venv/bin/activate

2. Instalar dependencias típicas de Odoo:
   pip install odoo==17.0
   pip install psycopg2-binary
   pip install requests
   pip install python-dateutil

3. Generar requirements.txt:
   pip freeze > requirements.txt

4. Mira el contenido:
   cat requirements.txt
   
   Verás algo como:
   -----------
   Babel==2.14.0
   click==8.1.7
   colorama==0.4.6
   cryptography==41.0.7
   docutils==0.20.1
   ebaysdk==2.1.5
   ...
   odoo==17.0
   psycopg2-binary==2.9.9
   python-dateutil==2.8.2
   requests==2.31.0
   ...
   -----------

5. Bonus - Reproducir en otra máquina:
   # En otra máquina/carpeta:
   git clone mi_proyecto
   cd mi_proyecto
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
   # Tendrá exactamente las mismas versiones
"""


# =============================================================================
# NOTAS IMPORTANTES SOBRE SOLUCIONES
# =============================================================================

"""
✅ PATRONES CLAVE QUE HAS VISTO:

1. DECORADOR BÁSICO:
   - @wraps(func) ← Preserva metadatos
   - Estructura: externo → wrapper
   - Retorna wrapper

2. DECORADOR CON PARÁMETROS:
   - Estructura de 3 niveles: parámetros → decorador → wrapper
   - Los parámetros se "cierran" en el decorador (closure)

3. CONTADOR/ESTADO:
   - Variable en el scope del decorador
   - nonlocal para modificarla
   - Persiste entre llamadas

4. CACHÉ:
   - Diccionario que persiste
   - Clave única para cada combinación de argumentos
   - Primero en caché, luego calcula

5. VALIDACIÓN:
   - Validar ANTES de ejecutar (números positivos)
   - O DESPUÉS de ejecutar (resultado en rango)

💡 CONSEJOS:
- Los decoradores son "wrappers" de funciones
- Se usan mucho en Odoo (@api.depends, @api.onchange, etc.)
- Practica hasta entenderlos bien
- No memorices, ENTIENDE la lógica
"""

print("\n✅ TODAS LAS SOLUCIONES DEL DÍA 5 COMPLETADAS")