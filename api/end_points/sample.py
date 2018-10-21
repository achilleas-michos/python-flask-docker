from flask import Blueprint, Response
from api.common.json_response import json_response


sample_api = Blueprint('sample_api', __name__)


@sample_api.route('/', methods=['GET'])
def main():
    return Response('Main sample endpoint')


@sample_api.route('/<int:id>', methods=['GET'])
def get(id):
    return json_response({'Id': id}, 200)
