from flask import request, Blueprint
from api.common.json_response import json_response


echo_api = Blueprint('echo_api', __name__)


@echo_api.route('/', methods=['POST'])
def echo():
    req_data = request.get_json()
    return json_response(req_data, 201)