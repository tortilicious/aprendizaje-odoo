from functools import wraps
from time import time, sleep
import random


# Ejercicio 1: Decorador básico
def saludar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hola")
        resultado = func(*args, **kwargs)
        print("Adios")
        return resultado

    return wrapper


@saludar
def saludo_nombre(nombre):
    return f"Hola {nombre}"


# saludo = saludo_nombre("Miguel")
# print(saludo)


# Ejercicio 2: Preservando el valor de retorno
def duplicar_resultado(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 2

    return wrapper


@duplicar_resultado
def calcular_precio(precio_base):
    return precio_base * 1.10


# print(calcular_precio(100)) # Resultado esperado: 220


# Ejercicio 3: Manejando argumentos
def validar_positivo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            for arg in args:
                if arg <= 0:
                    raise ValueError("Valor negativo o nulo")
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error capturado en el wrapper: {e}"

    return wrapper


@validar_positivo
def dividir(num1, num2):
    return num1 / num2


# print(dividir(10, -2))


# Ejercicio 4: Decorador con contador
def contar_llamadas(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"La función ha sido llamada {wrapper.contador}")
        wrapper.contador += 1
        return func(*args, **kwargs)

    wrapper.contador = 1
    return wrapper


@contar_llamadas
def procesar_datos():
    print("Procesando datos")


# procesar_datos()
# procesar_datos()
# procesar_datos()
# procesar_datos()


# Ejercicio 5: Decorador Logging
def log_ejecucion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tiempo_inicial = time()

        print(f"\n=== Ejecutando función: {func.__name__} ===")

        if args:
            print(f"Argumentos posicionales: {args}")

        if kwargs:
            print(f"Argumentos nombrados: {kwargs}")

        resultado = func(*args, **kwargs)

        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial

        print(f"Resultado: {resultado}")
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
        print("=" * 40)

        return resultado

    return wrapper


class Usuario:
    id_contador = 1

    def __init__(self, nombre):
        self.nombre = nombre
        self.id = Usuario.id_contador
        Usuario.id_contador += 1
        self.activo = True


usuario1 = Usuario("Miguel")
usuario2 = Usuario("Maria")
usuario3 = Usuario("Juan")
usuario3.activo = False

lista_usuarios = [usuario1, usuario2, usuario3]


@log_ejecucion
def buscar_usuario(id_usuario, incluir_inactivos=False):
    sleep(0.5)  # Simula una operación lenta

    for usuario in lista_usuarios:
        if not usuario.activo and not incluir_inactivos:
            continue

        if usuario.id == id_usuario:
            return {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "activo": usuario.activo
            }

    return None


# Pruebas
# resultado1 = buscar_usuario(1, True)
# print(f"\nResultado final: {resultado1}\n")
#
# resultado2 = buscar_usuario(3, incluir_inactivos=False)
# print(f"\nResultado final: {resultado2}\n")



# Ejercicio 6: Decorador Retry
def reintentar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        excepcion = None
        for intento in range (1, 4):
            try:
                print(f"Intento {intento} de 3")
                resultado = func(*args, **kwargs)
                print(f"Éxito en la conexión. Intento: {intento}")
                return resultado
            except Exception as e:
                print(f"Intento {intento} falló: reintentando establecer conexión...")
                excepcion = e

        print("Se han agotado todos los intentos de conexión.")
        raise excepcion
    return wrapper


@reintentar
def conectar_api():
    sleep(1)
    if random.random() < 0.7:
        raise TimeoutError("No se ha podido establecer la conexión.")
    return "Conexión realizada con éxito"

try:
    conectar_api()
except TimeoutError as e:
    print(e)
