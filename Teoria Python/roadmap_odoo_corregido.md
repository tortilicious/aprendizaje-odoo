# Roadmap de Preparación: Prácticas en Desarrollo ERP con Odoo

**Estudiante:** DAM (Desarrollo de Aplicaciones Multiplataforma)  
**Objetivo:** Preparación para prácticas de desarrollo ERP en Odoo  
**Inicio de prácticas:** Finales de noviembre 2025  
**Duración estimada de preparación:** 3-4 semanas  
**Estado actual:** Día 5-7 (Python avanzado + Odoo básico)

---

## Contexto y Punto de Partida

### Conocimientos actuales
- ✅ Fundamentos sólidos de programación
- ✅ Experiencia con Java/Kotlin (POO, patrones de diseño)
- ✅ Python básico completado (Día 1-2)
- ✅ POO en Python completada (Día 2-4)
- ⚠️ Conocimientos limitados de Python avanzado
- 🆕 Sin experiencia previa en Odoo

### Ventajas desde Java/Kotlin
- ✅ Conoces POO (clases, herencia, polimorfismo)
- ✅ Familiarizado con frameworks (similar a cómo Odoo estructura módulos)
- ✅ Experiencia con bases de datos y ORMs
- ✅ Conoces patrones MVC/MVVM
- ✅ Entiendes decoradores (equivalentes a anotaciones Java)

---

## Objetivos de Aprendizaje

### Semana 1: Fundamentos de Python (5-7 días) ✅ COMPLETADA

**Días 1-2:** Sintaxis básica y diferencias con Java
- [x] Variables y tipos de datos (tipado dinámico vs estático)
- [x] Estructuras de control (if, for, while)
- [x] Comprensión de listas (similar a streams en Java)
- [x] Funciones y argumentos (args, kwargs)
- [x] Manejo de excepciones (try/except vs try/catch)

**Días 3-4:** POO en Python
- [x] Clases y objetos (diferencias con Java)
- [x] Herencia y composición
- [x] Propiedades y decoradores (@property)
- [x] Métodos especiales (__init__, __str__, __repr__)
- [x] Herencia múltiple (no existe en Java)

**Días 5-7:** Python para Desarrollo Web/ERP
- [ ] Módulos y paquetes (import)
- [ ] Trabajar con diccionarios (muy usado en Odoo)
- [ ] List comprehensions y generadores (avanzado)
- [ ] Decoradores (fundamentales en Odoo)
- [ ] Context managers (with statement)
- [ ] Virtualenv y gestión de dependencias (pip)
- [ ] Conexiones a bases de datos (conceptual)

**Proyecto mini:**
```python
# Crear un CRUD simple en consola
# Gestión de inventario con:
# - Añadir productos
# - Listar productos
# - Actualizar stock
# - Eliminar productos
# (Usar archivos JSON para persistencia)
```

---

### Semana 2: Introducción a Odoo (7 días)

#### Día 1-2: Entorno y Arquitectura
- [ ] Instalar Odoo en modo desarrollo
- [ ] Entender la estructura de Odoo (arquitectura MVC)
- [ ] Explorar la interfaz y módulos estándar
- [ ] Activar modo desarrollador
- [ ] Comprender el ORM de Odoo

**Setup inicial:**
```bash
# Instalación de Odoo (Linux/macOS)
git clone https://github.com/odoo/odoo.git
cd odoo
pip install -r requirements.txt
./odoo-bin --addons-path=addons -d mi_database
```

**Recursos:**
- Documentación oficial: https://www.odoo.com/documentation/17.0/
- Tutorial para desarrolladores: https://www.odoo.com/documentation/17.0/developer.html

#### Día 3-4: Estructura de Módulos
- [ ] Crear tu primer módulo
- [ ] Entender el archivo __manifest__.py
- [ ] Estructura de directorios (models, views, security, data)
- [ ] Comprender las dependencias entre módulos

**Primer módulo:**
```
mi_biblioteca/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── libro.py
├── views/
│   └── libro_views.xml
└── security/
    └── ir.model.access.csv
```

**Ejercicio:**
```python
# Crear módulo "Gestión de Biblioteca"
# - Modelo: Libro (título, autor, ISBN, disponible)
# - Vistas básicas (tree, form)
# - Permisos de acceso
```

#### Día 5-6: Modelos y ORM
- [ ] Definir modelos (heredan de models.Model)
- [ ] Tipos de campos (Char, Integer, Many2one, One2many)
- [ ] Relaciones entre modelos
- [ ] Métodos de búsqueda y escritura
- [ ] Decoradores @api (similar a anotaciones Java)

**Conceptos clave:**
```python
from odoo import models, fields, api

class Producto(models.Model):
    _name = 'mi.producto'
    _description = 'Producto'
    
    name = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio')
    categoria_id = fields.Many2one('mi.categoria', 'Categoría')
    
    @api.depends('precio')
    def _compute_precio_con_iva(self):
        for rec in self:
            rec.precio_iva = rec.precio * 1.21
```

**Proyecto:**
```python
# Expandir módulo biblioteca:
# - Añadir modelo Préstamo
# - Relacionar con Libro y Cliente (res.partner)
# - Implementar lógica de préstamo/devolución
# - Calcular multas por retraso
```

#### Día 7: Vistas y Acciones
- [ ] Tipos de vistas (tree, form, kanban, search)
- [ ] XML para definir vistas
- [ ] Acciones de ventana
- [ ] Menús y submenús
- [ ] Widgets especiales

**Ejemplo de vista:**
```xml
<record id="view_libro_form" model="ir.ui.view">
    <field name="name">libro.form</field>
    <field name="model">biblioteca.libro</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="autor"/>
                    <field name="isbn"/>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

---

### Semana 3: Desarrollo Avanzado en Odoo (7 días)

#### Día 1-2: Herencia y Extensión
- [ ] Herencia de modelos (_inherit)
- [ ] Extensión de vistas (xpath)
- [ ] Sobrescribir métodos
- [ ] Añadir campos a modelos existentes

**Ejercicio:**
```python
# Extender el modelo res.partner (contactos):
# - Añadir campo "socio_numero"
# - Añadir campo "fecha_alta"
# - Extender la vista form para mostrar nuevos campos
```

#### Día 3-4: Lógica de Negocio
- [ ] Restricciones (constraints)
- [ ] Valores por defecto
- [ ] Computed fields
- [ ] Onchange methods
- [ ] Workflow y estados

**Proyecto:**
```python
# Módulo "Gestión de Pedidos Simple"
# - Estados: borrador, confirmado, enviado, entregado
# - Botones para cambiar estados
# - Restricciones: no borrar pedidos confirmados
# - Cálculo automático de totales
# - Onchange de producto para rellenar precio
```

#### Día 5: Seguridad y Permisos
- [ ] Grupos de acceso
- [ ] Reglas de registro (record rules)
- [ ] Archivo ir.model.access.csv
- [ ] Permisos por campo

**Configuración:**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_producto_user,producto_user,model_mi_producto,base.group_user,1,0,0,0
access_producto_manager,producto_manager,model_mi_producto,base.group_system,1,1,1,1
```

#### Día 6-7: Reportes e Integraciones
- [ ] QWeb templates
- [ ] Reportes PDF básicos
- [ ] Wizards (asistentes)
- [ ] Acciones servidor
- [ ] API externa básica (controllers)

**Mini-proyecto:**
```python
# Crear informe PDF de préstamos
# Crear wizard para renovar préstamos masivamente
# Crear endpoint JSON para consultar disponibilidad
```

---

### Semana 4: Práctica Real y Refinamiento (5-7 días)

#### Proyecto Final Integrador: "Sistema de Gestión de Inventario y Ventas"

Características:
- [ ] Gestión de productos (con categorías y variantes)
- [ ] Control de stock (movimientos de entrada/salida)
- [ ] Gestión de proveedores
- [ ] Pedidos de compra
- [ ] Alertas de stock mínimo
- [ ] Reportes básicos

Este proyecto integra:
- ✅ Modelos relacionados
- ✅ Herencia y extensión
- ✅ Lógica de negocio compleja
- ✅ Vistas personalizadas
- ✅ Permisos y seguridad
- ✅ Reportes

#### Día 6-7: Debugging y Buenas Prácticas
- [ ] Logging en Odoo
- [ ] Debugging con PyCharm/VS Code
- [ ] Testing básico
- [ ] Convenciones de código Odoo
- [ ] Git para módulos Odoo

---

## Herramientas Recomendadas

### IDE
- **VS Code** con extensiones:
  - Python
  - Odoo Snippets
  - XML Tools
- **PyCharm Community** (alternativa robusta)

### Entorno de desarrollo
```bash
# Estructura recomendada
~/odoo-dev/
├── odoo/              # Core de Odoo (git clone)
├── custom-addons/     # Tus módulos personalizados
├── venv/             # Entorno virtual Python
└── config/           # Archivos de configuración
```

### Comandos útiles
```bash
# Iniciar Odoo con debug
./odoo-bin -c mi_config.conf --dev=all

# Actualizar módulo
./odoo-bin -c mi_config.conf -u mi_modulo -d mi_database

# Instalar módulo
./odoo-bin -c mi_config.conf -i mi_modulo -d mi_database
```

---

## Recursos de Referencia

### Documentación Esencial
1. **Documentación oficial Odoo 17**: https://www.odoo.com/documentation/17.0/
2. **ORM API**: https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html
3. **Guía de desarrollo**: https://www.odoo.com/documentation/17.0/developer/tutorials.html

### Comunidad y Ayuda
- Forum oficial: https://www.odoo.com/forum
- GitHub Odoo: https://github.com/odoo/odoo
- Stack Overflow (tag: odoo)

### Comparación Python vs Java/Kotlin
| Concepto | Java/Kotlin | Python |
|----------|-------------|--------|
| Definir clase | `public class Producto {}` | `class Producto:` |
| Constructor | `public Producto() {}` | `def __init__(self):` |
| Herencia | `extends` | `(ParentClass)` |
| Importar | `import com.example.Clase` | `from module import Class` |
| Null | `null` | `None` |
| Boolean | `true/false` | `True/False` |
| Arrays/Listas | `List<String>` | `list` o `[]` |
| Diccionarios | `Map<K,V>` | `dict` o `{}` |

---

## Complementos Adicionales para tu Situación (Día 5-7)

Considerando que ya estás en el Día 5-7, he añadido algunos temas que te faltarían:

### Python Avanzado (Días 5-7) - IMPORTANTE PARA ODOO

#### Decoradores (CRÍTICO para Odoo)
```python
# Decorador personalizado
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Antes de ejecutar {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Después de ejecutar {func.__name__}")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")

# En Odoo usarás mucho:
# @api.depends('campo1', 'campo2')
# @api.onchange('campo')
# @api.constrains('campo')
```

#### Generadores y Expresiones Generadoras
```python
# Generador (lazy evaluation)
def numeros_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Expresión generadora
pares = (i for i in range(10) if i % 2 == 0)
```

#### Context Managers (with statement)
```python
# Importante para manejo de conexiones en Odoo
with open('archivo.txt') as f:
    contenido = f.read()  # Archivo se cierra automáticamente

# Crear custom context manager
from contextlib import contextmanager

@contextmanager
def mi_contexto():
    print("Entrando")
    try:
        yield
    finally:
        print("Saliendo")

with mi_contexto():
    print("Dentro del contexto")
```

#### Manejo Avanzado de Diccionarios
```python
# Muy usado en Odoo para vals, context, etc.
from collections import defaultdict

# defaultdict
d = defaultdict(list)
d['items'].append('valor1')

# Desempaquetado avanzado
datos = {'nombre': 'Juan', 'edad': 30, 'email': 'juan@email.com'}
{**datos, 'ciudad': 'Madrid'}  # Merge de dicts

# Comprehension avanzado
{k: v for k, v in datos.items() if v != 'Juan'}
```

#### Expresiones Lambda y Funciones de Orden Superior
```python
# Usadas en Odoo con search, filter, sorted
numeros = [1, 2, 3, 4, 5]

# Lambda con map
pares = list(map(lambda x: x * 2, numeros))

# Lambda con sorted
personas = [('Ana', 25), ('Luis', 30), ('María', 20)]
sorted(personas, key=lambda x: x[1])

# Lambda con filter
mayores_3 = list(filter(lambda x: x > 3, numeros))
```

#### Type Hints (Recomendado para código limpio)
```python
# Muy útil en Odoo para documentación
def calcular_total(precio: float, cantidad: int) -> float:
    return precio * cantidad

# Con tipos complejos
from typing import List, Dict, Optional

def procesar_datos(items: List[Dict[str, str]]) -> Optional[int]:
    if not items:
        return None
    return len(items)
```

---

## Checklist Final Pre-Prácticas

### Conocimientos Técnicos
- [x] Sintaxis básica de Python
- [x] POO en Python
- [ ] Python avanzado (decoradores, generadores, context managers)
- [ ] Crear módulos Odoo desde cero
- [ ] Definir modelos y relaciones
- [ ] Crear vistas (tree, form, kanban)
- [ ] Implementar lógica de negocio
- [ ] Configurar permisos
- [ ] Heredar y extender módulos existentes
- [ ] Debugging básico en Odoo
- [ ] Testing básico
- [ ] SQL básico (para queries en Odoo)

### Proyecto Demostrable
- [ ] Al menos 2-3 módulos completos y funcionales
- [ ] Código en GitHub/GitLab
- [ ] README con instalación y uso
- [ ] Comentarios en el código
- [ ] Pruebas unitarias básicas

### Preparación Soft Skills
- [ ] Preguntas preparadas sobre el stack tecnológico de la empresa
- [ ] Portfolio actualizado con proyecto Odoo
- [ ] LinkedIn actualizado con nuevas skills (Python, Odoo)
- [ ] Ganas de aprender y adaptarte
- [ ] Experiencia en debugging y resolución de problemas

---

## Consejos Finales

### Durante la preparación
1. **No te agobies**: Python es más simple que Java en muchos aspectos
2. **Practica diariamente**: Mejor 2 horas diarias que 14 horas el sábado
3. **Documenta tu código**: Te ayudará a repasar
4. **Haz preguntas**: Usa la documentación oficial y comunidades
5. **Instala Odoo ya**: Comienza a explorar la interfaz y estructura

### En las prácticas
1. **Pregunta sin miedo**: Es mejor preguntar que hacer suposiciones
2. **Toma notas**: Cada empresa tiene sus convenciones
3. **Lee el código existente**: Aprenderás mucho del código del equipo
4. **Pide feedback**: Mejora continua
5. **Versiona todo**: Git es tu amigo

### Ventajas que ya tienes (como programador Java/Kotlin)
- ✅ Entiendes POO perfectamente
- ✅ Sabes trabajar con frameworks y estructuras MVC
- ✅ Conoces patrones de diseño
- ✅ Experiencia con IDEs y debugging
- ✅ Sabes trabajar con bases de datos y ORMs

**Solo necesitas adaptar esos conocimientos a Python y Odoo. ¡Vas a estar bien preparado!**

---

## Tracking de Progreso

### Semana 1: Python ✅ COMPLETADA
- [x] Día 1-2: Sintaxis básica
- [x] Día 3-4: POO
- [x] Día 5-7: Python avanzado + proyecto

### Semana 2: Odoo Básico (EN PROGRESO)
- [ ] Día 1-2: Setup y arquitectura
- [ ] Día 3-4: Primer módulo
- [ ] Día 5-6: ORM y modelos
- [ ] Día 7: Vistas

### Semana 3: Odoo Avanzado (PRÓXIMAMENTE)
- [ ] Día 1-2: Herencia
- [ ] Día 3-4: Lógica de negocio
- [ ] Día 5: Seguridad
- [ ] Día 6-7: Reportes

### Semana 4: Proyecto Final (PRÓXIMAMENTE)
- [ ] Día 1-5: Desarrollo proyecto integrador
- [ ] Día 6-7: Refinamiento y buenas prácticas

---

**¡Mucho éxito en tus prácticas! 🚀**

*Recuerda: Este roadmap es una guía. Ajusta el ritmo según tu tiempo disponible y aprendizaje. Lo importante es entender los conceptos, no memorizar sintaxis.*

---

**Última actualización:** 05/11/2025  
**Próximo checkpoint:** Acabar Python avanzado e iniciar Odoo  
**Duración estimada hasta prácticas:** 2-3 semanas