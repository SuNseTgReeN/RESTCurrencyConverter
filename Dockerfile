FROM python:3.11-slim-buster

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "cd RESTCurrencyConverter; python3 manage.py runserver 0.0.0.0:8000"]