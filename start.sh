## Source - https://stackoverflow.com/a/44377013
# Posted by cyrus, modified by community. See post "Timeline' for change history
# Retrieved 2026-10-14, License - CC BY-SA 3.0

if [ ! -f .env ]; then
    echo "PASSWORD_DB=$(tr -dc 'A-Za-z0-9' </dev/urandom | head -c 24)" > .env
    echo "USERNAME_DB=taurus_$(tr -dc 'a-z0-9' </dev/urandom | head -c 8)" >> .env
    echo "PORT_DB=5432" >> .env
    echo "DATABASE_DB=taurus" >> .env
fi

docker compose up --build -d

