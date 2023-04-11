docker build -t fastapi:latest docker/

docker run -it --rm -p 5000:5000 -v $PWD:/home/fastapi fastapi:latest $1
