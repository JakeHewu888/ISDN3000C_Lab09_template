The movie is in /movie

Build docker image: 
docker build -t flask_container_image .

docker run -d \
    -p 5001:5000 \
    --name flask-container_instance \
    -v "$(pwd)/FlaskApp/database.db:/app/database.db" \
    flask_container_image

after:
http://localhost:5001

docker-compose up --build
http://localhost

docker stop flask-container_instance
docker rm flask-container_instance