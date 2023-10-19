# Curso-Programacion-Orientado-Objetos-UNEMI
curso de Programación orientado a Objetos con Python

## Plantilla Inicial Docker, python 3.10 y Django 4.

1. Copiar el contenido del archivo `.env.example` en un nuevo archivo `.env`

## En caso de no utilizar Docker, podéis utilizar entorno virtual venv (SOLO LA PRIMERA VEZ)

        1. python -m venv venv
        2. source venv/Scripts/activate
        3. python -m pip install --upgrade pip
        4. pip install -r venv-requirements.txt

        Resumido:
        (opcion 1): python -m venv venv && source venv/Scripts/activate ... (concatenar los comandos con &&)
        (opcion 1): Make install-virtual

A partir de ahora asegurate de estar dentro del entorno virtual (venv):

        source venv/Scripts/activate

### Creamos el proyecto Django

        1. mkdir django-backend
        2. django-admin startproject app django-backend/.

        Resumido: Make init-project

## Levantar servicio Django dentro de entorno virtual venv
        1. cd django-backend/
        2. set -a; source ../.env; set +a
        3. python manage.py runserver 0.0.0.0:8001

        Abrir navegador: http://localhost:8001/

### Levantar servicio Django dentro de entorno virtual venv, con comando Make

        Make runserver

## Pasos para la migración en Base de datos.
Asegurate de estar dentro de la carpeta del projecto Django: django-backend/

        1. python manage.py migrate
        2. python manage.py createsuperuser

Con estos pasos de habra creado el modulo de seguridad del admin de Django.

### Pasos para crear modulos o aplicaciones en Django
Asegurate de estar dentro de la carpeta del projecto Django: django-backend/

        python manage.py startapp name_app

No olvidar agregar el nombre del nuevo app en el archivo settings.py

        INSTALLED_APPS = [
           ...,
           'name_app',
        ]

### Pasos para la migración cuando se realizan cambios en los models.
Asegurate de estar dentro de la carpeta del projecto Django: django-backend/

        1. python manage.py makemigrations
        2. python manage.py migrate

### Levantando el Servidor Django:
Asegurate de estar dentro de la carpeta del projecto Django: django-backend/

        1. set -a; source ../.env; set +a
        2. python manage.py runserver 0.0.0.0:8001

        Abrir navegador: http://localhost:8001/

![Optional Text](./capturas/run-server-django.PNG)


## Caso de estudio - modelo UML de ventas.

![Optional Text](./capturas/ventas-uml.PNG)
