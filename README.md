# Reservation App

## build and run container via docker-compose (--build ensures images are rebuilt)

`docker-compose up --build`

## to run just the postgres service, detached

`docker-compose up -d postgres`

## to seed the database

`python db/seed_script.py`
