"""
Ejercicio B:
Con esta lista: ["python", "java", "javascript", "kotlin"]

Crea lista con longitud de cada palabra
Crea lista solo con palabras que contengan "java"
Crea lista con palabras en mayúsculas
"""


# Ejercicio B
lenguajes = ["python", "java", "javascript", "kotlin"]


def longitud_palabra(lenguajes):
    return [len(palabra) for palabra in lenguajes]


def filtrar_java(lenguajes):
    return [palabra for palabra in lenguajes if "java" in palabra]


def palabras_mayusculas(lenguajes):
    return [palabra.upper() for palabra in lenguajes]