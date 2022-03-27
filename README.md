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

## Notes

This project is a quick test of some technologies, which are not my main stack, so there are probably many things to improve.

#### Why FastAPI?

Usually, for large projects I use Django, and for specific services I use Bottle or Flask. However, I had been hearing about FastAPI and its [performance](https://christophergs.com/python/2021/06/16/python-flask-fastapi/) for some time, so I wanted to try it out.

#### No ORMs?

I had external motivations to try to do the project without any ORMs.

#### These migrations files? What the heck?

I was considering whether to make a command to migrate and populate the database or do it more automatically, and finally I decided to make a basic migration system without relying on third party packages. It's a basic approach and can be improved a lot, but for this test I think is enough. For serious projects I would use an ORM anyway.

#### Unittest? Why not pytest?

It is the package I usually work with and I started testing before I saw that most of the FastAPI examples use pytest. In case of redoing the project I would definitely try pytest.

#### Auth?

I have finally decided to add a basic authentication system, however, passwords are not encrypted in the DB and the method is not my preferred one. With more time I would add a JWT with httpOnly cookies.

#### "adm1" endpoint is slow af

I know, I know. It's because an aggregation of surfaces is made and for each surface an aggregation of another table is made. I have tried some optimization but I have not achieved anything. With more time I would modify the tables or make some materialized view.

#### Adm1?

Nomenclature for first-level [administrative divisions](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country)

#### So many folders...

Yes, it's true, for this project it wasn't necessary to have so many folders, but... What if it grows?

#### Anything else?

For the next project with FastAPI I will spend a lot of time reading its documentation (which is very good) in order to do less messing around.