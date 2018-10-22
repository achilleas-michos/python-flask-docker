from flask import Blueprint
from flask_restplus import Api
from .sample.sample import ns as sample_ns


blueprint = Blueprint('api', __name__, url_prefix='/api')


api = Api(blueprint,
          title='Example API with REST-plus',
          version='1.0',
          description='An Api structure to develop your projects'
         )

api.add_namespace(sample_ns, path='/sample')
