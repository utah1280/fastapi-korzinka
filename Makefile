run:
	python fastapi-application/main.py

docker-up:
	sudo docker-compose up -d

docker-down:
	sudo docker-compose down