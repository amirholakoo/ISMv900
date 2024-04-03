
From A to Z setup Linux servers and running services.
    

## Installation:

### Update:

    sudo apt-get update

    sudo apt-get upgrade

### Change directory:

    cd ~/V9/v988/

### Rename old folder:

admin@raspberrypi:~/V9/v988 $ `mv ISMv900 ISMv900_old_$(date +%Y%m%d%H%M%S)`

### Delete old venv:

admin@raspberrypi:~/V9/v988 $ `rm -r venv`

### Clone new repo:

admin@raspberrypi:~/V9/v988 $ `git clone https://github.com/amirholakoo/ISMv900.git`

### NOTE:  This command changes the ownership of all files and directories within venv and ISMv900 to the current user and group:

`sudo chown -R $USER:$USER ISMv900`
`sudo chown -R $USER:$USER venv`

### Install Python:

admin@raspberrypi:~/V9/v988 $ `sudo apt-get install python3 python3-pip`

### Install Virtual Env:

sudo pip3 install virtualenv

### Create/Activate/Deactivate venv:

(venv) admin@raspberrypi:~/V9/v988 $ `python3 -m venv venv`

activate:

`source venv/bin/activate`

deactivate:

`deactivate`

### Install Django:

(venv) admin@raspberrypi:~/V9/v988/ISMv900 $ `pip install django`

OR

pip install -r requirements.txt

### Install jdatetime:

(venv) admin@raspberrypi:~/V9/v988/ISMv900 $ `pip install jdatetime`

### Create static/dist in ISMv900 root

|- myapp

|- frontend

.

.

.

|- static

	L---dist
 

(venv) admin@raspberrypi:~/V9/v988/ISMv900 $ mkdir -p static/dist

### Run Django Server:

    python manage.py runserver

access:

    http://localhost:8000
    
**Stop the server:**

    Crtl+C

## BackEnd:

### Make Migrations:

    python manage.py makemigrations

### Make Migrate:

    python manage.py migrate

### Make Migrations for myapp:

    python manage.py makemigrations myapp

### Make Migrate for myapp:

    python manage.py migrate myapp

OR

	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations myapp
	python manage.py migrate myapp

### Run Django Server:

    python manage.py runserver

### Create users:

    python manage.py createsuperuser

### Access:

--- python manage.py runserver @ http://127.0.0.1:8000/

## FrontEnd:

### Change directory:

    cd frontend

### Download and Install npm:

Download packages:

    sudo apt install npm -y

Installing:

    npm install

### Run Vue.js Server:

    npm run serve

### Install and Run PostgreSQL

Install PostgreSQL: The installation steps vary depending on your operating system.

`sudo apt-get update`

`sudo apt-get install postgresql postgresql-contrib`

Start PostgreSQL service (if not already running):

`sudo service postgresql start`

Create a PostgreSQL User and Database:

`sudo -u postgres psql`

`CREATE DATABASE mydatabase;`

`CREATE USER admin WITH ENCRYPTED PASSWORD 'pi';`

`GRANT ALL PRIVILEGES ON DATABASE mydatabase TO admin;`

`\q`

** find your venv and activate:**

`source venv/bin/activate`

`sudo apt-get install libpq-dev`

`pip install psycopg2`

### Configure Your Django

Modify settings.py: Update the DATABASES setting in `myapp` Django project's `settings.py` file:

**If you can't find it in myapp directory then**

`sudo nano settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'admin',
        'PASSWORD': 'pi',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Replace `mydatabase`, `admin`, and `pi` with your PostgreSQL database and user credentials.


### Transfer Your Data

Export Data from SQLite: Use Django's `dumpdata` command to export your existing data:

`python manage.py dumpdata > data.json`

Migrate Your Models: Apply your migrations to the new PostgreSQL database:

`python manage.py migrate`

Import Data to PostgreSQL: Load the data you exported from SQLite into PostgreSQL:

`python manage.py loaddata data.json`

### Windows SETUP:

Clone: git clone https://github.com/amirholakoo/ISMv900.git

`python -m venv venv`

`venv\Scripts\activate`

`pip install -r requirements.txt`

`sudo apt-get install libpq-dev'

`pip install psycopg2'

`mkdir static/dist`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py makemigrations myapp`

`python manage.py migrate myapp`

`python manage.py createsuperuser`

`cd frontend`

`npm install`

`npm run serve`

`cd..`

`python manage.py runserver`

