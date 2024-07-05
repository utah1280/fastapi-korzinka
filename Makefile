docker-up:
	sudo docker-compose up -d

docker-down:
	sudo docker-compose down

docker-psql:
	sudo docker exec -it postgres psql -U root -d korzinka