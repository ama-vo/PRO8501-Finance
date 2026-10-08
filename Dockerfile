FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY ./TaurusCapital /app/

CMD ["python3", "manage.py", "makemigration"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "TaurusCapital.wsgi:application"]


