# Install or update needed software
sudo apt-get update
sudo apt-get install -yq git supervisor python python-pip python3-distutils
sudo pip install --upgrade pip virtualenv

# Fetch source code
export HOME=/root
sudo git clone https://github.com/tamharo/goliv-api.git  /opt/app/search


# Account to own server process
useradd -m -d /home/pythonapp pythonapp

# Python environment setup
virtualenv -p python3 /opt/app/search/env
/bin/bash -c "source /opt/app/search/env/bin/activate"
/opt/app/search/env/bin/pip install -r /opt/app/search/requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/app/search

# Put supervisor configuration in proper place
cp /opt/app/search/python-app.conf /etc/supervisor/conf.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update