# This Python script setups InfluenceAPI development environment
# It assumes the OS is Ubuntu Linux

import os
os.system('sudo apt-get install python-setuptools')
os.system('sudo easy_install virtualenv')
os.system('cd $HOME; virtualenv --no-site-packages venv')
os.system('source ~/venv/bin/activate; pip install -r requirements.txt; python manage.py syncdb; python manage.py migrate; python manage.py runserver 0.0.0.0:8000')
