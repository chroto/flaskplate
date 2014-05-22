#! /bin/env python

import sys
import os

project = "flaskplate"
BASE_DIR = os.path.join(os.path.dirname(__file__))

activate_this = os.path.join(BASE_DIR, "env/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from flaskplate.app import create_app
application = create_app(config=os.environ.get('APP_CONFIG',
                                               'flaskplate.config.ProductionConfig'))
