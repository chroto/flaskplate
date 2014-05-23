"""
Functional Test Suite to assert everything is working OK.
"""
from flask.ext.testing import TestCase

from flaskplate.app import create_app
from flaskplate.config import TestConfig


class TestFront(TestCase):

    def create_app(self):
        return create_app(TestConfig)

    def test_frontpage(self):
        response = self.client.get('/')
        self.assert_200(response)
        self.assert_template_used('index.html')
        return response

    def test_help_page(self):
        response = self.client.get('/help')
        self.assert_200(response)
        self.assert_template_used('frontend/footers/help.html')
        return response
