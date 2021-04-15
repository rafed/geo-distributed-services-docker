FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

# EXPOSE 8080

CMD ["python", "/app/server.py"]