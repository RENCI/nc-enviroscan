# nc-enviroscan test

This repository contains the software for creating the NC Enviroscan web map application. It consists of a 
Django Rest Framwork (DRF)/Postgres/PostGIS backend for serving data, and a Vue/Quasar/Openlayers front end
for displaying and interacting with the maps.

# Development 

## Build docker images and containers for the backend

After downloading or cloning the repository, change your directory to the project root directory:

cd nc-enviroscan

In the project root directory create a file named .env.dev and add the following information to it:

DEBUG=1  
SECRET_KEY=foo  
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]  
SQL_ENGINE=django.contrib.gis.db.backends.postgis  
SQL_DATABASE=ncenviroscan_dev  
SQL_USER=ncenviroscan  
SQL_PASSWORD=xxxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres  

Add your own password.

In the next step, from the project root directory run docker-compose on the development docker-compose.yml file:

docker-compose up -d --build

After this process has finished run "python manage.py migrate" using the docker-compose command:

docker-compose exec web python manage.py flush --no-input

At this poing the database is ready for ingest of data.

## Build docker images and containers for the frontend

In the next step change your directory to the quasar directory:

cd quasar

Next run docker-compose on the development docker-comose.yml file:

docker-compose up -d --build

After the containers have been created, the map will be accessible using the URL:

http://localhost:8081/

The maps MapBox Satellite baselayer requires a token. To get this token you will need to go to the MapBox 
web site and create an account. After you have the token edit the secrets.json file in:

src/assests/secrets.json

adding the token to the MB_KEY line.

# Productions

## Build docker images and containers for the backend

After downloading or cloning the repository, change your directory to the project root directory:

cd nc-enviroscan

In the project root directory create a file named .env.prod and add the following information to it:

DEBUG=0  
SECRET_KEY=change_me  
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]  
SQL_ENGINE=django.contrib.gis.db.backends.postgis  
SQL_DATABASE=ncenviroscan_prod  
SQL_USER=ncenviroscan  
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres  

Add your own password. Know create a file named .env.prod.db and add the following information to it:

POSTGRES_USER=ncenviroscan  
POSTGRES_PASSWORD=xxxxxxxxx  
POSTGRES_DB=ncenviroscan_prod  

Add your own password.

In the next step, from the project root directory run docker-compose on the production docker-compose.prod.yml file:

docker-compose -f docker-compose.prod.yml up -d --build

After this process has finished run "python manage.py migrate" using the docker-compose command:

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

At this poing the database is ready for ingest of data.

## Build docker images and containers for the frontend

In the next step change your directory to the quasar directory:

cd quasar

Next run docker-compose on the production docker-comose.prod.yml file:

docker-compose -f docker-compose.prod.yml up -d --build

After the containers have been created, the map will be accessible using the URL:

http://localhost:80/

The maps MapBox Satellite baselayer requires a token. To get this token you will need to go to the MapBox
web site and create an account. After you have the token edit the secrets.json file in:

src/assests/secrets.json

adding the token to the MB_KEY line.

