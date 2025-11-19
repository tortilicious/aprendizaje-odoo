
# Ejercicio 2. Control de flujo - Calculadora de descuentos
DESCUENTO_5 = 0.05
DESCUENTO_10 = 0.1
DESCUENTO_15 = 0.15
DESCUENTO_MAX = 0.25
CLIENTE_VIP = True


def calcular_descuento(precio, vip):
    # Validación entrada
    if precio < 0:
        print("El precio no puede ser negativo")
        return 0
    if precio < 20:
        descuento = 0
    elif precio < 50:
        descuento = DESCUENTO_5
    elif precio < 100:
        descuento = DESCUENTO_10
    else:
        descuento = DESCUENTO_15

    # Duplicar si es VIP
    if vip:
        descuento *= 2
    if descuento > DESCUENTO_MAX:
        descuento = DESCUENTO_MAX

    print(f"Descuento aplicado: {descuento * 100}%")
    return precio * (1 - descuento)