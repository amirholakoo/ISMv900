# chmod +x deploy.sh
# ./deploy.sh


#!/bin/bash

# Stop Django Server if running
pkill -f runserver

# Update and upgrade the system packages
sudo apt-get update
sudo apt-get upgrade -y

# Change to the specified directory and rename the old directory
cd ~/V9/v988/
if [ -d "ISMv900" ]; then
    mv ISMv900 ISMv900_old_$(date +%Y%m%d%H%M%S)  # Rename with a timestamp
fi

# Clone the repository
git clone https://github.com/amirholakoo/ISMv900.git v988

# Install Python and pip if they are not installed
sudo apt-get install python3 python3-pip -y

# Change ownership of the venv directory
sudo chown -R $USER:$USER ~/ISMv900/venv
# Or sudo chown -R admin:admin ~

# Install virtualenv if not installed
sudo pip3 install virtualenv

# Create a virtual environment and activate it
cd v988
python3 -m venv venv
source venv/bin/activate

# Install Django and other dependencies
pip install django
# pip install -r requirements.txt  # If you have a requirements.txt file
pip install jdatetime

# Create static/dist directories
mkdir -p myapp/frontend/static/dist

# Apply Django migrations
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations myapp
python manage.py migrate myapp

# Create a superuser
echo "Creating superuser..."
python manage.py createsuperuser --noinput || true  # Adjust or remove this line based on your need

# Run the Django development server
python manage.py runserver &

# Change directory to frontend and set up Vue.js
cd ../frontend

# Install npm and dependencies
sudo apt install npm -y
npm install

# Run Vue.js server
npm run serve

echo "Deployment script executed successfully."
