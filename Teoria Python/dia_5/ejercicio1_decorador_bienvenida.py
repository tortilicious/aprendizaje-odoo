from functools import wraps

def decorador_bienvenida(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Antes de ejecutar {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Despues de ejecutar {func.__name__}")
        return resultado
    return wrapper


@decorador_bienvenida
def crear_usuario(nombre, email):
    return {'nombre': nombre, 'email': email}


resultado_wrapper = crear_usuario("Miguel", "miguel@correo.es")
print(resultado_wrapper)
print(crear_usuario.__name__)