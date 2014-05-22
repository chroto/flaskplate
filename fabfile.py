# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html

from fabric.api import local

project = "flaskplate"


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
