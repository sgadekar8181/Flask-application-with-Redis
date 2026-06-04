FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 app:app
