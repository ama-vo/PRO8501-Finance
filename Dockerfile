FROM python:3.12-slim

LABEL authors="joliott"

WORKDIR /app

RUN pip install --no-cache-dir django yfinance

EXPOSE 8000

COPY ./TaurusCapital /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


