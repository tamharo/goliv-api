set -ev

# Install or update needed software
apt-get update
apt-get install -yq git supervisor python python-pip python3-distutils
pip install --upgrade pip virtualenv

# Fetch source code
export HOME=/root
git clone https://github.com/tamharo/goliv-api.git  /opt/app/goliv

# Install Cloud Ops Agent
sudo bash /opt/app/goliv/add-google-cloud-ops-agent-repo.sh --also-install

# Account to own server process
useradd -m -d /home/pythonapp pythonapp

# Python environment setup
sudo virtualenv -p python3 /opt/app/goliv/env
sudo /bin/bash -c "source /opt/app/goliv/env/bin/activate"
sudo /opt/app/goliv/env/bin/pip install -r /opt/app/goliv/requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/app

# Put supervisor configuration in proper place
cp /opt/app/goliv/python-app.conf /etc/supervisor/conf.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update