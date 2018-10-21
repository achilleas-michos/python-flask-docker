from flask import Flask
from flask_restful import Resource, Api
from .config import get_config
from .end_points import sample_api, echo_api


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(get_config(environment))

    api = Api(app)

    class Status(Resource):
        def get(self):
            return 'Server is running!'

    api.add_resource(Status, '/')

    app.register_blueprint(sample_api, url_prefix='/api/sample')
    app.register_blueprint(echo_api, url_prefix='/api/echo')

    return app
