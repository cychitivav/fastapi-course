docker build -t fastapi:latest docker/

docker run -it --rm --net=host -v $PWD:/home/fastapi fastapi:latest
