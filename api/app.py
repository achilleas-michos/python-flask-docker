from flask import Flask
from api.config import get_config
from api.modules.api import blueprint as api


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(get_config(environment))

    app.register_blueprint(api)

    return app


if __name__ == '__main__':
    app = create_app('development')
    app.run(port=8080)
