# Ejercicio 1 - Acceso seguro

# def obtener_valor_seguro(diccionario, clave1, clave2 = None):
#     if diccionario.get(clave1) is None:
#         return None
#     elif clave2 is None:
#         return diccionario.get(clave1)
#     else:
#         return diccionario.get(clave1).get(clave2)
#
# # Prueba:
# datos = {"usuario": {"edad": 20, "ciudad": "Madrid"}}
# print(obtener_valor_seguro(datos, "usuario", "edad"))  # 20
# print(obtener_valor_seguro(datos, "usuario", "nombre"))  # None
# print(obtener_valor_seguro(datos, "otros"))  # None


# # Ejercicio 2 - Transformación con Compresión
# def convertir_lista_a_diccionario(lista_de_tuplas):
#     return {k: v for k, v in lista_de_tuplas}
#
# # Prueba:
# datos = [("nombre", "Miguel"), ("edad", 20), ("ciudad", "Madrid")]
# resultado = convertir_lista_a_diccionario(datos)
# print(resultado)  # {'nombre': 'Miguel', 'edad': 20, 'ciudad': 'Madrid'}


# # Ejercicio 3 - Filtar Diccionario
# def filtrar_diccionario(diccionario, predicado):
#     return {k: v for k, v in diccionario.items() if predicado(k, v)}
#
# # Prueba:
# datos = {"a": 1, "b": 5, "c": 3, "d": 2}
#
# # Valores mayores que 2
# resultado1 = filtrar_diccionario(datos, lambda k, v: v > 2)
# print(resultado1)  # {'b': 5, 'c': 3}
#
# # Claves que contienen 'a'
# resultado2 = filtrar_diccionario(datos, lambda k, v: 'a' in k)
# print(resultado2)  # {'a': 1}

# # Ejercicio 4 - Fusionar y Deduplicar
# def fusionar_diccionarios(dict1, dict2, resolver_conflicto=None):
#     if resolver_conflicto is None:
#         dict1.update(dict2)
#         return dict1
#     else:
#         resultado = dict1.copy()
#         for clave in dict1.keys():
#             if clave in dict2.keys():
#                 resultado[clave] = resolver_conflicto(clave, dict1[clave], dict2[clave])
#         for clave in dict2.keys():
#             if clave not in dict1.keys():
#                 resultado[clave] = dict2[clave]
#         return resultado
#
#
# # Prueba 1: Sin resolver (default)
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 99, "c": 3}
# print(fusionar_diccionarios(dict1, dict2))
# # {'a': 1, 'b': 99, 'c': 3}
#
# # Prueba 2: Con resolver (toma el mayor)
# print(fusionar_diccionarios(dict1, dict2, lambda k, v1, v2: max(v1, v2)))
# # {'a': 1, 'b': 99, 'c': 3}
#
# # Prueba 3: Con resolver (concatena strings)
# dict1 = {"nombre": "Miguel", "apellido": "García"}
# dict2 = {"nombre": " López", "ciudad": "Madrid"}
# print(fusionar_diccionarios(dict1, dict2, lambda k, v1, v2: v1 + v2))
# # {'nombre': 'Miguel López', 'apellido': 'García', 'ciudad': 'Madrid'}


# Ejercicio 5 - Aplanar diccionario
def aplanar_diccionario(diccionario, prefijo=""):
    resultado = {}

    for clave, valor in diccionario.items():
        nueva_clave = f"{prefijo}_{clave}" if prefijo else clave

        if isinstance(valor, dict):
            resultado_recursivo = aplanar_diccionario(valor, nueva_clave)  # ← Capturas el resultado
            resultado.update(resultado_recursivo)  # ← Lo fusionas con resultado
        else:
            resultado[nueva_clave] = valor

    return resultado

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

diccionario_aplanado = aplanar_diccionario(datos)
print(diccionario_aplanado)
# {
#   'usuario_nombre': 'Miguel',
#   'usuario_edad': 20,
#   'usuario_contacto_email': 'miguel@example.com',
#   'usuario_contacto_telefono': '123456',
#   'ciudad': 'Madrid'
# }