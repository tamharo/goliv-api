# Install or update needed software
apt-get update
apt-get install -yq git supervisor python python-pip python3-distutils
pip install --upgrade pip virtualenv

# Fetch source code
export HOME=/root
git clone https://github.com/tamharo/goliv-api.git  /opt/app/search

# Install Cloud Ops Agent
sudo bash /opt/app/search/add-google-cloud-ops-agent-repo.sh --also-install

# Account to own server process
useradd -m -d /home/pythonapp pythonapp

# Python environment setup
sudo virtualenv -p python3 /opt/app/search/env
sudo /bin/bash -c "source /opt/app/search/env/bin/activate"
sudo /opt/app/search/env/bin/pip install -r /opt/app/search/requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/app

# Put supervisor configuration in proper place
cp /opt/app/search/python-app.conf /etc/supervisor/conf.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update