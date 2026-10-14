FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install django psycopg psycopg2 gunicorn

EXPOSE 8000

COPY ./TaurusCapital /app/

ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "TaurusCapital.wsgi:application"]


