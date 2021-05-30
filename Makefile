all:
	docker build -t flask-esdl-service .
	docker run -d -p 4000:4000 --name flask-esdl-service flask-esdl-service

stop:
	docker stop flask-esdl-service
	docker rm flask-esdl-service
	