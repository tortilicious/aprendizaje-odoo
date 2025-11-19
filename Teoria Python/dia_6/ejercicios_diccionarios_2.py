# Ejercicio 2 - Mapping con transformación de valores

def mapear_y_transformar(diccionario, mapa_transformaciones):
    """
    Mapea claves y transforma valores según funciones especificadas.

    Parámetros:
    - diccionario: datos originales
    - mapa_transformaciones: {clave_vieja: (clave_nueva, funcion_transformacion)}

    Ejemplo:
    datos = {"nombre_producto": "laptop", "precio_unitario": "999.99"}
    mapa = {
        "nombre_producto": ("name", str.upper),  # Convierte a mayúsculas
        "precio_unitario": ("list_price", float)  # Convierte a float
    }

    mapear_y_transformar(datos, mapa)
    → {"name": "LAPTOP", "list_price": 999.99}
    """
    # TODO: Itera sobre diccionario original
    # TODO: Si está en mapa_transformaciones:
    #       - Extrae clave_nueva y funcion_transformacion
    #       - Aplica la función al valor
    #       - Agrega con la clave nueva
    # TODO: Si no está, agrega sin transformar

    resultado = {}
    for clave, valor in diccionario.items():
        if clave in mapa_transformaciones:
            nueva_clave, funcion = mapa_transformaciones[clave]
            resultado[clave] = funcion(valor)
        else:
            resultado[clave] = valor

    return resultado





# Prueba 1: Producto con transformaciones
datos1 = {
    "nombre_producto": "laptop",
    "precio_unitario": "999.99",
    "cantidad_stock": "5",
    "activo": "true"
}

mapa1 = {
    "nombre_producto": ("name", str.upper),  # A mayúsculas
    "precio_unitario": ("list_price", float),  # A float
    "cantidad_stock": ("qty_available", int),  # A int
    "activo": ("active", lambda x: x.lower() == "true")  # A boolean
}

resultado1 = mapear_y_transformar(datos1, mapa1)
print(resultado1)
# {'name': 'LAPTOP', 'list_price': 999.99, 'qty_available': 5, 'active': True}

# Prueba 2: Cliente con transformaciones
datos2 = {
    "id_cliente": "101",
    "nombre_cliente": "miguel garcía",
    "saldo_deuda": "1500.50",
    "fecha_registro": "2025-01-15"
}

mapa2 = {
    "id_cliente": ("id", int),
    "nombre_cliente": ("name", str.title),  # Capitaliza: Miguel García
    "saldo_deuda": ("debt", float)
}

resultado2 = mapear_y_transformar(datos2, mapa2)
print(resultado2)
# {'id': 101, 'name': 'Miguel García', 'debt': 1500.5, 'fecha_registro': '2025-01-15'}