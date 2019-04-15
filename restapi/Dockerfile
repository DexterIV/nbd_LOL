FROM python:3.5

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["api.py"]

# build with "docker build -t docker_flask:latest ."
# run with "docker run -p 9043:9043 docker_flask"
