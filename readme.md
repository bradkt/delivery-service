## Delivery Service API

Seans Python3 Flask Rest Boilerplate

### To Setup and Start

```bash
add delivery-biz-firebase-adminsdk-f8kue-afc933be68.json to project ( in top level )
pip install -r requirements.txt
python app.py
```

## Docker

docker-compose up
http://127.0.0.1/swagger/

# Base URL for Docker = "http://127.0.0.1"

# Base URL for local build= "http://localhost:5000"

## Swagger UI

Hosted Locally
http://127.0.0.1:5000/swagger/

### Get List

```bash
curl -X GET http://127.0.0.1:5000/list/gqZAyy4RCFUd6I6yomYXx9BoaUf1

```

### Create List

```bash
curl -X POST http://127.0.0.1:5000/list/gqZAyy4RCFUd6I6yomYXx9BoaUf1
```

### Update List

```bash
curl -X PUT http://127.0.0.1:5000/list/gqZAyy4RCFUd6I6yomYXx9BoaUf1 -H 'Content-Type: application/json' -d '{"randString1":{"value":"apples","note":"red","quantity":5},"randString2":{"value":"banana","note":"ripe","quantity":6},"randString3":{"value":"limes","note":"large","quantity":2}}'
```

### Clear List

```bash
curl -X DELETE http://127.0.0.1:5000/list/gqZAyy4RCFUd6I6yomYXx9BoaUf1
```

## Unit Test with Nose

```bash
nosetests --verbosity=2
```

### Test Output

```bash
Test getting a list ... ok
Test getting a non existent list ... ok
Test adding a new list ... ok
Test update a list ... ok
Test updating a list with no user id ... ok
Test clearing list ... ok
Test clearing list fail ... ok

----------------------------------------------------------------------
Ran 7 tests in 15.013s

OK
```

###

Hosted via Docker-compose and Nginx
http://127.0.0.1/swagger/
