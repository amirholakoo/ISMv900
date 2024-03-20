# STOP SERVERS
# deactivate

# chmod +x deploy.sh
# ./deploy.sh


#!/bin/bash

# Stop Django Server if running
pkill -f runserver

# Update and Upgrade Packages
sudo apt-get update
sudo apt-get upgrade -y

# Navigate to the project directory
cd ~/V9/v988/

# Rename old project folder with a timestamp
mv ISMv900 "ISMv900_old_$(date +%Y%m%d%H%M%S)"

# Remove old virtual environment
rm -rf venv

# Clone new version of the project
git clone https://github.com/amirholakoo/ISMv900.git

# Change ownership of the new project folder and virtual environment (assuming they're already created at some point)
sudo chown -R $USER:$USER ISMv900

# Install Python3, pip, and virtualenv if not already installed
sudo apt-get install -y python3 python3-pip
sudo pip3 install virtualenv

# Create a new virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Install Django and jdatetime
pip install django
pip install jdatetime

# OR install all requirements from a file
# pip install -r requirements.txt

# Create static/dist directories in the project root
mkdir -p ISMv900/static/dist

# Navigate to the frontend directory
cd ISMv900/frontend

# Install npm and node packages
sudo apt install -y npm
npm install

# Instructions end here. Additional steps can be scripted based on requirements.
# For example, to run Django and Vue.js servers, you could add:
# Back in the project root
cd ..
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# Note: Automated superuser creation is complex and might require a separate script or manual process

# Starting servers (for demonstration, you'd typically use a more robust method in production)
# python manage.py runserver &
# cd frontend && npm run serve &
