import os
import unittest
from flask_script import Manager
from api.api import create_app


os.environ['FLASK_ENV'] = os.environ['ENVIRONMENT'] if 'ENVIRONMENT' in os.environ else 'development'
app = create_app(os.environ['FLASK_ENV'])

manager = Manager(app)

@manager.command
def run():
    app.run(port=8080)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()