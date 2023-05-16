ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up --build -d --remove-orphans
up:
	docker-compose up -d
down:
	docker-compose down
makemigrations:
	docker-compose run app python manage.py makemigration
migrate:
	docker-compose run app python manage.py migrate
superuser:
	docker-compose run app python manage.py createsuperuser
pytest:
	docker-compose run app pytest
