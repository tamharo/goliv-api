# Install or update needed software
apt-get update
apt-get install -yq git supervisor python python-pip python3-distutils
pip install --upgrade pip virtualenv

# Fetch source code
export HOME=/root
git clone  /opt/app


# Account to own server process
useradd -m -d /home/pythonapp pythonapp

# Python environment setup
virtualenv -p python3 env
/bin/bash -c "source env/bin/activate"
env/bin/pip install -r requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /

# Put supervisor configuration in proper place
cp python-app.conf /etc/supervisor/conf.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update