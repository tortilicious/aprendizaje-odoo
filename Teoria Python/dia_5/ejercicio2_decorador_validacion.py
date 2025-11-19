from functools import wraps

def solo_positivos(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"No es un número: {arg}")
            if arg < 0:
                raise ValueError(f"Número negativo: {arg}")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

@solo_positivos
def calcular_area(base, altura):
    return base * altura

@solo_positivos
def calcular_precio_con_descuento(precio, descuento):
    return precio - descuento

area = calcular_area(10, 20)
print(area)

descuento = calcular_precio_con_descuento(100, "awdawd")
print(descuento)