# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html

from fabric.api import local, cd, prefix
import os

project = "flaskplate"
BASE_DIR = os.path.join(os.path.dirname(__file__))


def setup():
    """
    Setup virtual env.
    """
    local("virtualenv env")
    activate_env()
    local("python setup.py install")

def activate_env():
    """
    Activate this application's virtualenv
    """
    activate_this = "env/bin/activate_this.py"
    execfile(activate_this, dict(__file__=activate_this))


def run():
    """
    Runs the application in development mode.
    """
    activate_env()
    local("python manage.py run")

def setup_deploy():
    with cd(BASE_DIR):
        uwsgi_dir = os.path.join('env', 'etc', 'uwsgi'),
        dirs = [
            uwsgi_dir,
            os.path.join('env', 'tmp'),
            os.path.join('env', 'run'),
            os.path.join('env', 'log')
        ]
        map(lambda x: local('mkdir -p {0}'.format(x)), dirs)
        uwsgi_cfg = '''
    [uwsgi]
    chdir={BASE_DIR}
    http-socket=:9000
    module=flaskplate.wsgi
    callable=application
    processes=1
    threads=2
    home={env_dir}
    '''.format(BASE_DIR=BASE_DIR,
              env_dir=os.path.join(BASE_DIR, 'env')
              )
        with open(os.path.join(uwsgi_dir, 'flaskplate.ini'), 'w') as f:
            f.write(uwsgi_cfg)

def deploy():
    activate = os.path.join(BASE_DIR, 'env', 'bin', 'activate')
    with prefix('. {activate}'.format(activate=activate)):
        local('uwsgi --master \
              --die-on-term \
              --pidfile=env/var/run/flaskplate.pid \
              --ini env/etc/uwsgi/flaskplate.ini')

