# Ejercicio 4 - Filtrar y Transformar Diccionarios

usuarios = {
    'ana@email.com': {'nombre': 'Ana', 'edad': 25, 'activo': True},
    'luis@email.com': {'nombre': 'Luis', 'edad': 30, 'activo': False},
    'maria@email.com': {'nombre': 'María', 'edad': 20, 'activo': True},
}

def usuarios_activos(usuarios):
    # TODO: Retorna solo usuarios con activo=True
    # Resultado: {'ana@email.com': {...}, 'maria@email.com': {...}}
    return {k: v for k, v in usuarios.items() if v['activo']}

def mayores_de(usuarios, edad_minima):
    # TODO: Retorna usuarios con edad >= edad_minima
    return {k: v for k, v in usuarios.items() if v['edad'] >= edad_minima}

def obtener_nombres(usuarios):
    # TODO: Retorna lista de nombres
    # Resultado: ['Ana', 'Luis', 'María']
    return [v['nombre'] for k, v in usuarios.items()]


# Pruebas:
print(usuarios_activos(usuarios))
print(mayores_de(usuarios, 25))
print(obtener_nombres(usuarios))