import os
from contextlib import contextmanager


# Ejercicio 1

# class Cronometro:
#     def __enter__(self):
#         print("Iniciando...")
#         self.momento_incial = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         momento_final = time.time()
#         tiempo_transcurrido = momento_final - self.momento_incial
#         print(tiempo_transcurrido)
#         print(f"exc_type: {exc_type}")
#         print("Finalizando...")
#         return True
#
#
# with Cronometro() as cronometro:
#     time.sleep(2)
#     print("Trabajando...")
#     raise ValueError("Forzamos un error")


# Ejercicio 2

# class ArchivoSeguro:
#     def __init__(self, ruta):
#         self.ruta = ruta
#         self.archivo = None
#
#     def __enter__(self):
#         try:
#             self.archivo = open(self.ruta, 'r')
#             print(f"Archivo encontrado {self.ruta}")
#             return self.archivo
#         except FileNotFoundError as e:
#             print(f"Archivo no encontrado. Ruta: {self.ruta}")
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.archivo is not None:
#             self.archivo.close()
#         else:
#             print(exc_type, exc_val, exc_tb)
#
#
# # Prueba 1: archivo que existe
# with ArchivoSeguro("existe.txt") as f:
#     if f:
#         print("Contenido:", f.read())
#
# # Prueba 2: archivo que no existe
# with ArchivoSeguro("no_existe.txt") as f:
#     if f is None:
#         print("Archivo no disponible")
#
# # Prueba 3: error dentro del bloque
# try:
#     with ArchivoSeguro("existe.txt") as f:
#         if f:
#             numero = int(f.read())  # Error si no es número
# except ValueError:
#     print("Error capturado correctamente")


# Ejercicio 3
# class SuppressError:
#     def __init__(self, *excepciones_a_ignorar):
#         self.excepciones = excepciones_a_ignorar
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"[EXIT] exc_type: {exc_type}")
#         print(f"[EXIT] excepciones_a_ignorar: {self.excepciones}")
#
#         if exc_type is None:
#             print("[EXIT] No hay excepción, devolviendo False")
#             return False
#         elif exc_type in self.excepciones:
#             print(f"[EXIT] {exc_type.__name__} está en la lista, SILENCIANDO")
#             return True
#         else:
#             print(f"[EXIT] {exc_type.__name__} NO está en la lista, PROPAGANDO")
#             return False
#
#
#
# # Prueba 1: error ignorado
# with SuppressError(ValueError):
#     print("Antes del error")
#     raise ValueError("Este error será silenciado")
#     print("Después del error (no se ejecuta)")
#
# print("Continuamos después del context manager")
#
# # Prueba 2: error NO ignorado
# try:
#     with SuppressError(ValueError):
#         raise KeyError("Este error NO será silenciado")
# except KeyError:
#     print("Error propagado correctamente")


# Ejercicio 4

# @contextmanager
# def cronometro(nombre = "operacion"):
#     tiempo_inicial = time.time()
#     print(f"Iniciando cronometro: {tiempo_inicial}")
#     yield
#     tiempo_finalizacion = time.time()
#     tiempo_total = tiempo_finalizacion - tiempo_inicial
#     print(f"Finalizando cronometro: {tiempo_total}")
#
# with cronometro("descarga"):
#     time.sleep(1)
#     print("Descargando...")


# Ejercicio 5

@contextmanager
def cambiar_directorio(ruta):
    # Directorio original
    directorio_actual = os.getcwd()
    try:
        # Cambio directorio
        os.chdir(ruta)
        yield
    finally:
        # Vuelta al directorio original
        print(f"[FINALLY] Volviendo a: {directorio_actual}")
        os.chdir(directorio_actual)


print(f"Directorio actual: {os.getcwd()}")
try:
    with cambiar_directorio("/awdawdawdawdawd"):
        print(f'Directorio temporal: {os.getcwd()}')
except FileNotFoundError:
    print(f"Error capturado, pero volvemos a: {os.getcwd()}")
