# Install or update needed software
sudo apt-get update
sudo apt-get install -yq git supervisor python python-pip python3-distutils
sudo pip install --upgrade pip virtualenv

# Fetch source code
sudo export HOME=/root
sudo git clone https://github.com/tamharo/goliv-api.git  /opt/app/search

# Python environment setup
sudo virtualenv -p python3 /opt/app/search/env
sudo /bin/bash -c "source /opt/app/search/env/bin/activate"
sudo /opt/app/search/env/bin/pip install -r /opt/app/search/requirements.txt