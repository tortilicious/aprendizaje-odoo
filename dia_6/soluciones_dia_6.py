# ✅ SOLUCIONES COMENTADAS - DÍA 6: GENERADORES, CONTEXT MANAGERS, DICCIONARIOS
# ==============================================================================

"""
IMPORTANTE: 
- Estas son SOLUCIONES COMENTADAS
- Pueden haber otras formas correctas
- Lo importante es ENTENDER el concepto
- Practica hasta que lo domines
"""

# =============================================================================
# EJERCICIO 1: Generador Rango Personalizado
# =============================================================================

def rango_personalizado(inicio, fin, paso):
    """
    Generador que produce números en rango personalizado.
    
    Concepto clave: yield
    - yield pausa la función y retorna un valor
    - La próxima llamada a next() reanuda desde donde se pausó
    """
    actual = inicio
    
    # Caso 1: paso positivo (ir de menor a mayor)
    if paso > 0:
        while actual < fin:
            yield actual
            actual += paso
    
    # Caso 2: paso negativo (ir de mayor a menor)
    elif paso < 0:
        while actual > fin:
            yield actual
            actual += paso
    
    else:
        raise ValueError("❌ El paso no puede ser 0")


# Prueba
print("--- Ejercicio 1: Generador Rango ---")

print("De 0 a 10 en pasos de 2:")
for num in rango_personalizado(0, 10, 2):
    print(num, end=" ")  # 0 2 4 6 8

print("\n\nDe 10 a 0 en pasos de -2:")
for num in rango_personalizado(10, 0, -2):
    print(num, end=" ")  # 10 8 6 4 2

print("\n")


# =============================================================================
# EJERCICIO 2: Generador de Líneas CSV
# =============================================================================

def leer_csv(ruta_archivo):
    """
    Generador que lee archivo CSV línea por línea.
    
    Ventaja: No carga TODO el archivo en memoria
    - Si el archivo tiene 1 millón de líneas, procesa una a una
    - Ideal para archivos grandes
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                # Dividir por comas y eliminar espacios/saltos de línea
                fila = linea.strip().split(',')
                yield fila
    except FileNotFoundError:
        print(f"❌ Archivo {ruta_archivo} no encontrado")


# Para la prueba, necesitamos crear el archivo primero
print("--- Ejercicio 2: Generador CSV ---")

# Crear archivo de prueba
contenido_csv = """nombre,edad,ciudad
Ana,25,Madrid
Luis,30,Barcelona
María,28,Valencia"""

with open('datos.csv', 'w') as f:
    f.write(contenido_csv)

# Ahora leer con el generador
print("Leyendo archivo línea por línea:")
for fila in leer_csv('datos.csv'):
    print(fila)

# Limpiar
import os
os.remove('datos.csv')


# =============================================================================
# EJERCICIO 3: Generador Filtrado - Números Primos
# =============================================================================

def numeros_primos_hasta(n):
    """
    Generador que produce números primos hasta n.
    
    Concepto: Un número es primo si solo es divisible por 1 y por sí mismo.
    
    Estrategia:
    1. Para cada número de 2 a n
    2. Verificar si es primo
    3. Si es primo, yield
    """
    
    def es_primo(num):
        """Función auxiliar para verificar si es primo"""
        if num < 2:
            return False
        
        # Comprobar divisibilidad desde 2 hasta sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
    
    # Generar números primos
    for numero in range(2, n + 1):
        if es_primo(numero):
            yield numero


# Prueba
print("\n--- Ejercicio 3: Números Primos ---")

print("Primos hasta 30:")
for primo in numeros_primos_hasta(30):
    print(primo, end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29

print("\n")


# =============================================================================
# EJERCICIO 4: Generador Fibonacci Infinita
# =============================================================================

def fibonacci_infinito():
    """
    Generador que produce Fibonacci infinitamente.
    
    Importante:
    - NUNCA termina (generador infinito)
    - Se usa con break o cuando sabes que necesitas N valores
    - Cada valor se calcula solo cuando se pide
    """
    a, b = 0, 1
    
    while True:  # ← Bucle infinito
        yield a
        a, b = b, a + b  # Actualizar: (0,1) → (1,1) → (1,2) → (2,3) → ...


# Prueba
print("--- Ejercicio 4: Fibonacci Infinita ---")

fib = fibonacci_infinito()

print("Primeros 10 números de Fibonacci:")
for _ in range(10):
    print(next(fib), end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34

print("\n")


# =============================================================================
# EJERCICIO 5: Context Manager para Archivo Temporal
# =============================================================================

from contextlib import contextmanager
import tempfile
import os

@contextmanager
def archivo_temporal():
    """
    Context manager que crea y elimina archivo temporal automáticamente.
    
    Estructura:
    1. ANTES (yield): Crear archivo temporal
    2. DURANTE: Usar el archivo
    3. DESPUÉS (finally): Eliminar automáticamente
    """
    # Crear archivo temporal
    archivo_fd, ruta = tempfile.mkstemp()
    
    try:
        # Cerrar el file descriptor (para poder usarlo normalmente)
        os.close(archivo_fd)
        
        # yield retorna la ruta del archivo
        yield ruta
    
    finally:
        # Se ejecuta SIEMPRE, incluso si hay error
        if os.path.exists(ruta):
            os.remove(ruta)
            print(f"🗑️ Archivo temporal eliminado: {ruta}")


# Prueba
print("--- Ejercicio 5: Archivo Temporal ---")

# Usar el context manager
with archivo_temporal() as temp_file:
    print(f"✅ Archivo temporal creado: {temp_file}")
    
    # Escribir datos
    with open(temp_file, 'w') as f:
        f.write("Datos temporales de prueba")
    
    # Verificar que existe
    if os.path.exists(temp_file):
        print(f"📝 Archivo existe durante el with")

# Fuera del with, automáticamente se elimina
print(f"Archivo existe después del with: {os.path.exists(temp_file)}")  # False

print()


# =============================================================================
# EJERCICIO 6: Context Manager para Logging (Registro de Operaciones)
# =============================================================================

@contextmanager
def registrar_operacion(nombre_operacion):
    """
    Context manager que registra el ciclo de vida de una operación.
    
    Flujo:
    - ANTES: imprime inicio
    - DURANTE: ejecuta el código
    - ERROR: captura y registra
    - ÉXITO: registra éxito
    - SIEMPRE: registra fin (finally)
    """
    print(f"🔵 {nombre_operacion} iniciada")
    
    try:
        # El código dentro del with va aquí (yield)
        yield
        
        # Si llegamos aquí, fue exitoso
        print(f"✅ {nombre_operacion} completada")
    
    except Exception as e:
        # Hubo un error
        print(f"❌ {nombre_operacion} falló: {e}")
        # Relanzar la excepción para que se propague
        raise
    
    finally:
        # SIEMPRE se ejecuta (con éxito o error)
        print(f"🏁 {nombre_operacion} finalizada")


# Prueba
print("--- Ejercicio 6: Logging de Operaciones ---")

# Caso exitoso
print("\n1. Caso exitoso:")
with registrar_operacion("Lectura de BD"):
    print("  [Leyendo datos...]")

# Caso con error
print("\n2. Caso con error:")
try:
    with registrar_operacion("Escritura de BD"):
        print("  [Escribiendo datos...]")
        raise ValueError("Conexión perdida")
except ValueError:
    pass  # Ya fue registrado en el except del context manager

print()


# =============================================================================
# EJERCICIO 7: Context Manager para Límite de Tiempo
# =============================================================================

# Nota: Esta solución es simplificada (real sería más compleja)
# Para implementación real se usaría signal o threading

import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Operación tardó más de lo permitido")


@contextmanager
def limite_tiempo(segundos):
    """
    Context manager que pone un límite de tiempo.
    
    Nota: Solo funciona en Linux/macOS con signal
    Windows requiere otra estrategia (threading)
    """
    # Configurar el manejador de timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    
    # Establecer alarma
    signal.alarm(segundos)
    
    try:
        yield
    
    finally:
        # Cancelar alarma
        signal.alarm(0)


# Prueba (comentada porque signal no funciona bien en todos los sistemas)
print("--- Ejercicio 7: Límite de Tiempo ---")
print("(Solución solo funciona en Linux/macOS)")
print("Código disponible pero no probado en este entorno")

# import time
# 
# with limite_tiempo(2):
#     print("Operación rápida")
#     # Se completa antes de 2 segundos
# 
# with limite_tiempo(2):
#     print("Operación lenta")
#     time.sleep(5)  # ❌ TimeoutError


# =============================================================================
# EJERCICIO 8: Agrupar por Categoría (tipo Odoo)
# =============================================================================

from collections import defaultdict

def agrupar_por_categoria(productos):
    """
    Agrupa productos por categoría.
    
    Estrategia con defaultdict:
    - d = defaultdict(list)
    - Para cada producto, añadirlo a d[categoria]
    - Automáticamente crea la lista si no existe
    """
    agrupado = defaultdict(list)
    
    for producto in productos:
        categoria = producto['categoria']
        agrupado[categoria].append(producto)
    
    # Convertir a dict normal para retornar
    return dict(agrupado)


# Prueba
print("--- Ejercicio 8: Agrupar por Categoría ---")

productos = [
    {'nombre': 'Laptop', 'categoria': 'Electrónica', 'precio': 1200},
    {'nombre': 'Mouse', 'categoria': 'Accesorios', 'precio': 20},
    {'nombre': 'Monitor', 'categoria': 'Electrónica', 'precio': 300},
    {'nombre': 'Teclado', 'categoria': 'Accesorios', 'precio': 80},
]

resultado = agrupar_por_categoria(productos)

for categoria, items in resultado.items():
    print(f"\n{categoria}:")
    for item in items:
        print(f"  - {item['nombre']}: {item['precio']}€")


# =============================================================================
# EJERCICIO 9: Filtrar y Transformar Diccionarios
# =============================================================================

def usuarios_activos(usuarios):
    """Retorna solo usuarios activos"""
    return {
        email: datos 
        for email, datos in usuarios.items() 
        if datos['activo']
    }


def mayores_de(usuarios, edad_minima):
    """Filtra usuarios mayores de cierta edad"""
    return {
        email: datos 
        for email, datos in usuarios.items() 
        if datos['edad'] >= edad_minima
    }


def obtener_nombres(usuarios):
    """Retorna lista de nombres"""
    return [datos['nombre'] for datos in usuarios.values()]


def aplicar_descuento(usuarios, porcentaje):
    """Añade campo descuento a cada usuario"""
    resultado = {}
    
    for email, datos in usuarios.items():
        # Copiar datos originales y añadir descuento
        datos_con_descuento = {**datos, 'descuento': porcentaje}
        resultado[email] = datos_con_descuento
    
    return resultado


# Prueba
print("\n--- Ejercicio 9: Filtrar y Transformar Diccionarios ---")

usuarios = {
    'ana@email.com': {'nombre': 'Ana', 'edad': 25, 'activo': True},
    'luis@email.com': {'nombre': 'Luis', 'edad': 30, 'activo': False},
    'maria@email.com': {'nombre': 'María', 'edad': 20, 'activo': True},
}

print("1. Usuarios activos:")
print(usuarios_activos(usuarios))

print("\n2. Mayores de 25:")
print(mayores_de(usuarios, 25))

print("\n3. Nombres:")
print(obtener_nombres(usuarios))

print("\n4. Con descuento del 10%:")
con_descuento = aplicar_descuento(usuarios, 10)
for email, datos in con_descuento.items():
    print(f"  {email}: {datos}")


# =============================================================================
# EJERCICIO 10: Merge Inteligente de Configuraciones
# =============================================================================

def merge_configuraciones(default, proyecto, usuario):
    """
    Merge de configuraciones con precedencia.
    
    Precedencia (mayor a menor):
    1. usuario (más específico)
    2. proyecto
    3. default (más general)
    
    Estrategia: Empezar con default y sobrescribir
    """
    # Paso 1: Empezar con default
    resultado = default.copy()
    
    # Paso 2: Sobrescribir con proyecto
    resultado.update(proyecto)
    
    # Paso 3: Sobrescribir con usuario
    resultado.update(usuario)
    
    return resultado

# Alternativa más compacta (Python 3.9+):
# return {**default, **proyecto, **usuario}


# Prueba
print("\n--- Ejercicio 10: Merge Inteligente ---")

config_default = {
    'idioma': 'es_ES',
    'timezone': 'UTC',
    'debug': False,
}

config_proyecto = {
    'timezone': 'Europe/Madrid',
    'debug': True,
}

config_usuario = {
    'idioma': 'en_US',
}

resultado = merge_configuraciones(config_default, config_proyecto, config_usuario)

print("Configuración final:")
for clave, valor in resultado.items():
    print(f"  {clave}: {valor}")

# Resultado:
# idioma: en_US        (del usuario)
# timezone: Europe/Madrid  (del proyecto)
# debug: True          (del proyecto)


# =============================================================================
# EJERCICIO 11: Extraer y Renombrar Campos (Patrón Odoo)
# =============================================================================

def convertir_a_odoo(formulario):
    """
    Convierte diccionario de formulario a formato Odoo.
    
    Mapping de campos:
    - nombre_producto → name
    - precio_unitario → list_price
    - cantidad_stock → qty_available
    - codigo_barras → barcode
    """
    # Crear mapping (conversión)
    mapping = {
        'nombre_producto': 'name',
        'precio_unitario': 'list_price',
        'cantidad_stock': 'qty_available',
        'codigo_barras': 'barcode',
    }
    
    # Convertir
    resultado = {}
    for campo_antiguo, campo_nuevo in mapping.items():
        if campo_antiguo in formulario:
            resultado[campo_nuevo] = formulario[campo_antiguo]
    
    return resultado

# Alternativa con dict comprehension:
# def convertir_a_odoo(formulario):
#     mapping = {
#         'nombre_producto': 'name',
#         'precio_unitario': 'list_price',
#         'cantidad_stock': 'qty_available',
#         'codigo_barras': 'barcode',
#     }
#     return {
#         mapping[k]: v 
#         for k, v in formulario.items() 
#         if k in mapping
#     }


# Prueba
print("\n--- Ejercicio 11: Convertir a Odoo ---")

formulario = {
    'nombre_producto': 'Laptop',
    'precio_unitario': 1200,
    'cantidad_stock': 5,
    'codigo_barras': 'EAN123',
    'otro_campo': 'ignorado',  # No está en mapping
}

convertido = convertir_a_odoo(formulario)

print("Original:")
print(formulario)

print("\nConvertido a Odoo:")
print(convertido)


# =============================================================================
# NOTAS IMPORTANTES
# =============================================================================

"""
✅ PATRONES CLAVE:

1. GENERADORES (yield):
   - Procesar datos sin cargar todo en memoria
   - Perfectos para archivos grandes o secuencias infinitas
   - next() o for loop para consumir

2. GENERATOR EXPRESSIONS:
   - (x for x in lista)  ← Lazy evaluation
   - vs [x for x in lista]  ← Eager evaluation

3. CONTEXT MANAGERS (@contextmanager):
   - try/finally garantiza limpieza
   - yield divide: antes (setup) / durante (yield) / después (cleanup)
   - Usado para: archivos, conexiones, transacciones, locks

4. DICCIONARIOS AVANZADOS:
   - get() y setdefault() para acceso seguro
   - defaultdict() para crear automáticamente
   - Dict comprehensions para transformar
   - Merge con ** o |

5. AGRUPAR DATOS:
   - defaultdict(list) es tu amigo
   - Bucle simple: for item: d[key].append(item)

💡 CONSEJOS:
- Generadores: úsalos para procesar archivos grandes
- Context managers: úsalos para cualquier setup/cleanup
- Diccionarios: domina get(), defaultdict, comprehensions
- En Odoo: verás mucho dict con vals, context, domain
"""

print("\n✅ TODAS LAS SOLUCIONES DEL DÍA 6 COMPLETADAS")