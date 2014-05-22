# -*- coding: utf-8 -*-

from setuptools import setup

project = "flaskplate"

setup(
    name=project,
    version='0.1',
    description='Example Flask application',
    author='Chris Proto',
    author_email='cproto@sympoz.com',
    packages=[
        'flaskplate',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Script'
    ]
)
