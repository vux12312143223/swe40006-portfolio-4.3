# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /103806447-swe40006-portfolio-43

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]