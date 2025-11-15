# Mapping simple

def mapear_diccionario(diccionario, mapa):
    """
    Mapea las claves de un diccionario según un mapa.

    Parámetros:
    - diccionario: datos originales
    - mapa: diccionario con mapping {clave_vieja: clave_nueva}

    Retorna:
    - Nuevo diccionario con claves mapeadas

    Ejemplo:
    datos = {"nombre_producto": "Laptop", "precio_unitario": 999.99}
    mapa = {"nombre_producto": "name", "precio_unitario": "list_price"}

    mapear_diccionario(datos, mapa)
    → {"name": "Laptop", "list_price": 999.99}
    """
    # TODO: Itera sobre el diccionario original
    # TODO: Si la clave está en el mapa, usa la clave nueva
    # TODO: Si no está en el mapa, mantén la clave original
    resultado = {}

    for clave, valor in diccionario.items():
        if clave in mapa:
            nueva_clave = mapa[clave]
            resultado[nueva_clave] = valor
        else:
            resultado[clave] = valor

    return resultado

# Prueba 1: Mapping de producto
datos1 = {
    "nombre_producto": "Laptop",
    "precio_unitario": 999.99,
    "cantidad_stock": 5,
    "codigo_barras": "123456789"
}

mapa1 = {
    "nombre_producto": "name",
    "precio_unitario": "list_price",
    "cantidad_stock": "qty_available",
    "codigo_barras": "barcode"
}

resultado1 = mapear_diccionario(datos1, mapa1)
print(resultado1)
# {'name': 'Laptop', 'list_price': 999.99, 'qty_available': 5, 'barcode': '123456789'}

# Prueba 2: Mapping parcial (algunas claves no están en el mapa)
datos2 = {
    "id_cliente": 101,
    "nombre_cliente": "Miguel García",
    "email": "miguel@example.com",
    "telefonoContacto": "555-1234"
}

mapa2 = {
    "nombre_cliente": "name",
    "email": "email_address"
    # Nota: id_cliente y telefonoContacto NO están en el mapa
}

resultado2 = mapear_diccionario(datos2, mapa2)
print(resultado2)
# {'id_cliente': 101, 'name': 'Miguel García', 'email_address': 'miguel@example.com', 'telefonoContacto': '555-1234'}
