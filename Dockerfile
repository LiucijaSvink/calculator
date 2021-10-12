# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /calculator

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "calculator", "run", "--host=0.0.0.0"]