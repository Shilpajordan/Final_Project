## 1. Create .env file in main directory including this info:
	DB_NAME=meddb
	DB_USER=medadmin
	DB_PASSWORD=ma1234
	DB_HOST=127.0.0.1
	DB_PORT=5432


## 2. Create PostgreSQL database and user:
    sudo -u postgres psql

    CREATE DATABASE meddb;
    CREATE USER medadmin WITH PASSWORD 'ma1234';
    GRANT ALL PRIVILEGES ON DATABASE meddb TO medadmin;
    ALTER DATABASE meddb OWNER TO medadmin;

## 3. Make migrations:
	python manage.py makemigrations
	python manage.py migrate

## 4. Create superuser:
	python manage.py createsuperuser
	username: admin
	password: admin1234

## 5. Import doctors:
	connect to your database with dbeaver
	execute insert_doctors.sql