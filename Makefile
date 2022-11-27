MANAGE = src/manage.py
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8000
RUN_COMMAND = gunicorn-run

start:
	 $(MANAGE) runserver 0.0.0.0:8000

mm:
	$(MANAGE) makemigrations

m:
	$(MANAGE) migrate

user:
	$(MANAGE) createsuperuser

lint:
	flake8 ./src

check:
	$(MANAGE) check

check-migrate:
	$(MANAGE) --check --dry-run

shell_plus:
	$(MANAGE) shell_plus --print-sql

celery:
	 cd src && celery -A core worker -l info

beat_celery:
	 cd src && celery -A core beat -l info

flower_celery:
	cd src &&  celery -A core flower

freeze:
	pip freeze > requirements.txt

gunicorn-run:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/src core.wsgi --timeout 30 --log-level debug --max-requests 10000

collect-static:
	python src/manage.py collectstatic

gunicorn-run-sock:
	gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir $(PROJECT_DIR)/src core.wsgi --timeout 30 --log-level debug --max-requests 10000

pytest:
	cd src && pytest

test-all-project:
	cd src && pytest --cov=blog --cov-report=html --cov-fail-under=59

# DOCKER COMMANDS

doc-clear:
	 docker system prune -a

container:
	docker container ls -a

image:
	docker image ls -a

ps:
	docker-compose ps

docker-run-dev:
	$(eval  RUN_COMMAND=run)
	docker-compose up -d --build
	make copy-static

docker-run-production:
	$(eval RUN_COMMAND=gunicorn-run)
	docker-compose up -d --build
	make copy-static

docker-down:
	docker-compose down

docker-up:
	docker-compose up

copy-static:
	docker exec -it blog-backend python ./src/manage.py collectstatic --noinput
	docker cp blog-backend:/srv/project/static_content/static /tmp/static
	docker cp /tmp/static nginx:/etc/nginx
