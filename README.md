# Electricity-API

This project exposes API endpoints to user's electricity consumption details

## Tools & Frameworks Used
1. Django
2. Django REST Framework
3. Djoser (for API based token exposure)
4. Black (python code formatter)
5. Pytest (Unit test framework)

## API Documentation

Go to the project root and run the below command.

```shell script
docker run -p 80:8080 -e SWAGGER_JSON=/opt/swagger.json -v $(pwd):/opt swaggerapi/swagger-ui
```

Open `http://localhost` in the browser to see Swagger UI

## Prerequisites
* Python 3 or above
* minikube (with ingress addon enabled)
* kubectl command line utility
* Docker engine
 
## Build Server Image

```shell script
eval $(minikube docker-env)
docker build -t <tag> .
docker build -t baktha/myapi:0.0.1 .
```


## Deploy to minikube

Update image tag inside `kubernetes/server.yaml`

```shell script
eval $(minikube docker-env)
kubectl create -f kubernetes/server.yaml
kubectl port-forward service/api 9000:9000 > /dev/null 2>&1
```

#### New User Creation
New users can be created from the page `http://localhost:9000/auth/users`

## How to start the app Locally

* Go to the project root
* Create new python virtual environment `python3 -m venv venv`
* Activate the virtual environment `source venv/bin/activate`
* Install dependencies `pip install -r requirements.txt`
* Run `gunicorn electricity_api.wsgi`

## Authentication & Authorisation
This project uses Django REST Framework Token Based authentication.

The user needs to provide the auth token as part of the API calls via the header

`Authorisation: Token <auth token>`

### How to obtain access token

Replace the credentials with appropriate values and run the below command

```shell script
curl -k -X POST -d "username=<username>&password=<password>" http://localhost:9000/auth/token/login
```


## Running tests

It has just the skeleton and did not find time to create tests

```shell script
python -m pytest tests
```

## Examples

```shell script
curl -H "Authorization: Token <auth token>"  http://localhost:9000/data/?start=2019-05-03&count=3&resolution=days

curl -H "Authorization: Token <auth token>"  http://localhost:9000/limits/
```

## Assumptions
1. Provided DB data is copied into the container image and all the urls are served with given data
2. New user creations will end up creating user-ids in the backend
3. Users with matching user ids on the provided table dumps will be able to see results via the API


## Project Execution

**Task**|**Duration (Hrs)**
:-------:|:-----:
Requirement Analysis|0.5
Frameworks Research|0.5
Play with Django REST Framework|1
Play with Djoser|1
Implementation|3
Documentation|1
Deployment|1