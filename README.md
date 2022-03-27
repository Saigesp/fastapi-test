# FastAPI test

Test project to get to know FastAPI. Requires **docker** and **docker-compose**.

It is designed to use as few dependencies as possible, for example by avoiding the use of an ORM.

## Install

Clone the repository and install Docker and Docker-compose (if needed).

## Run

(Linux) In the root folder, run:

```sh
$ docker-compose up --build
```
> If the database is empty it will migrate and populate the database


### Endpoints

FastAPI generates an automatic interactive API documentation with **Swagger** (http://127.0.0.1:8000/docs) and **ReDoc** (http://127.0.0.1:8000/redoc)

## Tests

Some tests have been programmed, which can be executed with the following command (it is necessary to have the project running):

```sh
sudo docker-compose exec web bash -c "python -m unittest discover"
```