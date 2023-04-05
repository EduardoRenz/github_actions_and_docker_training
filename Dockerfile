FROM ubuntu:latest

EXPOSE 8000

WORKDIR /app

COPY . .

CMD [ "python main.py" ]