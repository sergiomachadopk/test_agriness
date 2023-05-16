# Test Agriness

## Cloning the project

1.	Open your Shell or Terminal;
2.	Navigate to the folder you want to use to clone the project;
3. Run the command

```
git clone https://github.com/sergiomachadopk/test_agriness.git
```

## Starting server using Docker

1.	Open your Shell or Terminal;
2.	Navigate to the project folder;
3. Run the command

```
docker-compose up --build
```

Apply migrations

```
docker-compose run app python manage.py migrate
```

Create super user 

```
docker-compose run app python manage.py createsuperuser
```

To Run Tests

```
docker-compose run app python manage.py test
```
