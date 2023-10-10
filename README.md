# Curso-Programacion-Orientado-Objetos-UNEMI
curso de Programación orientado a Objetos con Python

Plantilla Inicial Docker, python 3.10 y Django 4.

1. Copiar el contenido del archivo `.env.example` en un nuevo archivo `.env`

2. Ejecutar los siguientes pasos:

        docker-compose build --no-cache
        docker-compose run --rm django django-admin startproject app .

3. Habilite las siguientes lineas en archivo `django-backend/Dockerfile` linea [30,31]:

        RUN ["chmod", "+x", "/app/docker/entrypoint.sh"]
        ENTRYPOINT ["/app/docker/entrypoint.sh"]

4. Vuelva a crear la Imagen Docker

        docker-compose build
        docker-compose up

5. Abre el navegador e ingresa:

        http://localhost:8001/

## Levantando el Servidor Django:

![Optional Text](./capturas/run-server-django.PNG)


## En caso de no utilizar Docker, podéis utilizar entorno virtual venv

        python -m venv venv
        source venv/Scripts/activate
        python -m pip install --upgrade pip
        pip install -r venv-requirements.txt

## Levantar servicio Django dentro de entorno virtual venv
        cd django-backend/
        set -a; source ../.env; set +a
        python manage.py runserver 0.0.0.0:8001
        Abrir navegador: http://localhost:8001/

## Levantar servicio Django dentro de entorno virtual venv, con comando Make
        Make runserver
