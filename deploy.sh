# STOP SERVERS
# deactivate

# chmod +x deploy.sh
# ./deploy.sh


#!/bin/bash

echo "Stop Django Server if running"
pkill -f runserver

echo " Update and Upgrade Packages"
sudo apt-get update
sudo apt-get upgrade -y

echo " Navigate to the project directory"
cd ~/V9/v988/

echo "Rename old project folder with a timestamp"
mv ISMv900 "ISMv900_old_$(date +%Y%m%d%H%M%S)"

echo " Clone new version of the project"
git clone https://github.com/amirholakoo/ISMv900.git

#echo " Remove old virtual environment"
#rm -rf venv
#


echo " Change ownership of the new project folder and virtual environment (assuming they're already created at some point)"
sudo chown -R $USER:$USER ISMv900

echo " Navigate to the ISM directory"
cd ISMv900

echo " Install Python3, pip, and virtualenv if not already installed"
sudo apt-get install -y python3 python3-pip
sudo pip3 install virtualenv

echo " Create a new virtual environment and activate it"
python3 -m venv venv
source venv/bin/activate

echo " Install Django and jdatetime"
pip install django
pip install jdatetime
pip install pandas
pip install openpyxl
pip install qrcode

# OR install all requirements from a file
#pip install -r requirements.txt

echo " Create static/dist directories in the project root"
mkdir -p static/dist

echo " Navigate to the frontend directory"
cd frontend

echo " Install npm and node packages"
sudo apt install -y npm
npm install

# Instructions end here. Additional steps can be scripted based on requirements.
# For example, to run Django and Vue.js servers, you could add:

echo " Back in the project root"
cd ..
echo "Migration..."
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations myapp
python manage.py migrate myapp
echo "Create user"
python manage.py createsuperuser
# Note: Automated superuser creation is complex and might require a separate script or manual process

echo " Starting servers "
python manage.py runserver &
cd frontend && npm run serve &
