docker.build:
	docker-compose build --force-rm

docker.start:
	docker-compose up app

install: 
	poetry install

activate: install
	poetry shell

start: activate
	bot start