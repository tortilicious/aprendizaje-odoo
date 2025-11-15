# 5 Conversion de Estructura

def convertir_formulario_a_odoo(formulario):
    """
    Convierte estructura de formulario a estructura Odoo.

    Mapping:
    - nombre_producto → name
    - precio_unitario → list_price
    - cantidad_stock → qty_available
    - codigo_barras → barcode

    Args:
        formulario: Diccionario con estructura de formulario

    Returns:
        Diccionario con estructura Odoo
    """
    # TODO: Crea un mapeo de claves
    # TODO: Transforma el diccionario usando el mapeo
    # TODO: Retorna el nuevo diccionario
    diccionario_resultado = {}
    diccionario_mapeo = {'nombre_producto': 'name', 'precio_unitario': 'list_price', 'cantidad_stock': 'qty_available', 'codigo_barras': 'barcode'}
    return {v: formulario[k] for k, v in diccionario_mapeo.items() if k in formulario}



# Prueba:
formulario = {
    'nombre_producto': 'Laptop Dell',
    'precio_unitario': 1200.50,
    'cantidad_stock': 15,
    'codigo_barras': '123456789'
}

resultado = convertir_formulario_a_odoo(formulario)
print(resultado)
# Esperado: {'name': 'Laptop Dell', 'list_price': 1200.50, 'qty_available': 15, 'barcode': '123456789'}