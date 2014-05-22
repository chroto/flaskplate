#! /bin/env python

import os

project = "flaskplate"

from flaskplate.app import create_app
application = create_app(config=os.environ.get('APP_CONFIG',
                                               'flaskplate.config.ProductionConfig'))
