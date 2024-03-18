
From A to Z setup Linux servers and running services.
    

## Installation:

### Update:

    sudo apt-get update

    sudo apt-get upgrade

### Change directory:

    cd ~/V9/v988/

### Clone:

    git clone https://github.com/amirholakoo/ISMv900.git

### Install Python:

    sudo apt-get install python3 python3-pip

### NOTE:  This command changes the ownership of all files and directories within venv to the current user and group:


    sudo chown -R $USER:$USER ~/ISMv900/venv

OR

    sudo chown -R admin:admin ~

### Install Virtual Env:

    sudo pip3 install virtualenv

### Create/Activate/Deactivate venv:

    python3 -m venv venv

activate:

    source venv/bin/activate

deactivate:

    deactivate

### Install Django:

    pip install django

OR

    pip install -r requirements.txt

### Install jdatetime:

    pip install jdatetime

### Create static/dist

myapp
frontend
static
|---dist
	
    mkdir static

	/dist

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

