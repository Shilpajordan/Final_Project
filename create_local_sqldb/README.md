## 1. Pull settings.py from main branch:

## 2. Create .env file in main directory including this info:
	DB_NAME=meddb
	DB_USER=medadmin
	DB_PASSWORD=ma1234
	DB_HOST=127.0.0.1
	DB_PORT=5432


## 3. Create PostgreSQL database and user:
    sudo -u postgres psql

    CREATE DATABASE meddb;
    CREATE USER medadmin WITH PASSWORD 'ma1234';
    GRANT ALL PRIVILEGES ON DATABASE meddb TO medadmin;
    ALTER DATABASE meddb OWNER TO medadmin;

## 4. Make migrations:
	python manage.py makemigrations
	python manage.py migrate

## 5. Create superuser:
	python manage.py createsuperuser
	username: admin
	password: admin1234

## 6. Import doctors:
	connect to your database with dbeaver
	execute insert_doctors.sql