# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html
from contextlib import contextmanager

from fabric.api import local, cd, prefix
import os

BASE_DIR = os.path.join(os.path.dirname(__file__))

project = "flaskplate"
activate = os.path.join(BASE_DIR, 'env', 'bin', 'activate')

@contextmanager
def virtualenv():
    with prefix('source {activate}'.format(activate=activate)):
        yield


def setup():
    """
    Setup virtual env.
    """
    local("virtualenv env")
    with virtualenv():
        local("python setup.py install")


def run():
    """
    Runs the application in development mode.
    """
    with virtualenv():
        local("python manage.py run")

def test():
    with virtualenv():
        local('python setup.py test')

def setup_deploy():
    with cd(BASE_DIR):
        uwsgi_dir = os.path.join('env', 'etc', 'uwsgi')
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
    with virtualenv():
        local('uwsgi --master \
              --die-on-term \
              --pidfile=env/var/run/flaskplate.pid \
              --daemonize=env/var/log/flaskplate.log \
              --ini env/etc/uwsgi/flaskplate.ini')

