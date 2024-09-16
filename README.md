# Django Web Project

## Contenidos

### 1. Creación del proyecto

Creación del proyecto. Un proyecto puede contener una o varias aplicaciones.

```python	
django-admin startproject WebProject
```

Nos movemos hacia la carpeta y creamos la apliación. Una aplicación se puede utilizar en diferentes proyectos.

```python
python manage.py startapp WebProjectApp
```

Comprobamos que funciona el servidor.

```python
python manage.py runserver
```

Es posible que te pida el siguiente comando.

```python
python manage.py migrate 
```

### 1. Estructura de las carpetas

**Web Project**
-`settings.py`. Debemos incluir un registro de cada una de nuestras apps.
- `urls.py`. Apunta al archivo de mismo nombre de cada una de las aplicaciones (en esta caso solo hay una). Es una forma de tener organizadas las urls. 

**Web Project App**
- `urls.py`. Contiene solo las urls de esta aplicación. 
- `views.py`. Creación de todas vistas. 