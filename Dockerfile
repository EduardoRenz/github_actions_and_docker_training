FROM python:latest

EXPOSE 8000

WORKDIR /app

ENV environment=default

COPY . .

RUN apt-get install python3
RUN apt-get update
RUN apt-get -y install python3-pip

RUN pip install -r requirements.txt

CMD [ "python main.py" ]