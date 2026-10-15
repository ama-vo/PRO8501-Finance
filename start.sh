#!/bin/sh

if [ ! -f .env ]; then
    touch .env

    password=$(tr -dc 'A-Za-z0-9!?%=' < /dev/urandom | head -c 24)

    echo "PASSWORD_DB=$password" >> .env
    echo "NAME_DB=taurus_db" >> .env
    echo "USERNAME_DB=taurus" >> .env
    echo "PORT_DB=5432" >> .env

fi

docker compose up --build