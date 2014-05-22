import logging
from flask import Blueprint, render_template, current_app

logger = logging.getLogger(__name__)

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    current_app.logger.debug('Do things here')
    return render_template('index.html')

@frontend.route('/help')
def help():
    current_app.logger.debug('Do things here')
    return render_template('frontend/footers/help.html', active="help")
