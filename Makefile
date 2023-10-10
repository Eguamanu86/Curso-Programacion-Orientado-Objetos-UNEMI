.PHONY: help
SHELL := /bin/bash

help:
	@echo 'We should add info about the commands here'

install-virtual:
	python -m venv venv && source venv/Scripts/activate && python -m pip install --upgrade pip && pip install -r venv-requirements.txt

init-project:
	source venv/Scripts/activate && mkdir django-backend && django-admin startproject app django-backend/.

runserver:
	source venv/Scripts/activate && cd django-backend && set -a; source ../.env; set +a && python manage.py runserver 127.0.0.1:8001
