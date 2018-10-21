import unittest
from flask import current_app
from flask_testing import TestCase
from api.wsgi import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('api.config.Development')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'development_key')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('api.config.Production')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()