FROM python:latest

EXPOSE 5000

WORKDIR /app

ENV environment=default

COPY . .

RUN apt-get install python3
RUN apt-get update
RUN apt-get -y install python3-pip

RUN pip install -r requirements.txt

RUN chmod +x app.py

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]"