build:
	docker rm $(docker ps -a -q) && \
	docker build -t back_django . && \
	docker run \
		--env-file ./.env \
		-p 8000:8000 \
		-v "$(pwd):/app" \
		--name \
		django \
		back_django

bash:
	docker exec -it django bash

makemigrations:
	docker exec django python manage.py makemigrations


migrate:
	docker exec django python manage.py migrate

server:
	docker exec -it django python manager.py runserver

start:
	docker start django

test:
	docker exec django pytest