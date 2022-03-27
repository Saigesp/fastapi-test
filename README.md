# FastAPI test

Test project to get to know FastAPI. Requires **docker** and **docker-compose**.

It is designed to use as few dependencies as possible, for example by avoiding the use of an ORM.

## Install

Clone the repository and install Docker and Docker-compose (if needed).

## Run

**Linux**: In the root folder, run:

```sh
$ docker-compose up --build
```
> If the database is empty it will be migrated and populated with data from `data` folder

Once builded, you can navigate to http://localhost:8000 and other endpoints.

### Auth

A basic HTTP auth is enabled. The application expects a header that contains a username and a password, and if it doesn't receive it, it returns an HTTP 401 "Unauthorized" error.

When you try to open the URL for the first time the browser will ask you for your username and password. The credentials are:

```
username: test
password: test
```

### Endpoints

```
/v1/postal_codes/?bounds={bounds}             geometries & total turnover from a given bounds box (map view)
/v1/paystats/age-gender/{postal_code_id}      turnover for a given postal code grouped by age and gender
/v1/paystats/time-gender/{postal_code_id}     turnover for a given postal code grouped by time and gender
/v1/adm1/{postal_code_prefix}                 agg. geometries and total turnover for a given postal code prefix
```

#### Examples

http://localhost:8000/v1/postal_codes/?bounds=-2.8087269,41.1884418,-4.6561026,40.0329219

- Get geometries and total turnover for all Comunidad de Madrid postal codes

http://localhost:8000/v1/postal_codes/?bounds=-3.7228258,40.3866711,-3.7240934,40.3860618

- Get the geometry and total turnover for Carabanchel neigborhood

http://localhost:8000/v1/paystats/age-gender/6288

- Get paystats records for Carabanchel neighborhood grouped by age and gender

http://localhost:8000/v1/paystats/time-gender/6288

- Get paystats records for Carabanchel neighborhood grouped by date and gender

http://localhost:8000/v1/adm1/28

- Get aggregate geometry and total turnover of all postal codes that starts with '28' (Comunidad de Madrid)

#### Documentation

FastAPI generates an automatic interactive API documentation with **Swagger** (http://127.0.0.1:8000/docs) and **ReDoc** (http://127.0.0.1:8000/redoc)

## Tests

Some tests have been programmed, which can be executed with the following command (it is necessary to have the project running):

```sh
sudo docker-compose exec web bash -c "python -m unittest discover"
```