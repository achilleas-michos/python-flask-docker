from flask import request
from flask_restplus import Resource
from .sample_dto import namespace as ns, sample_data
from .sample_logic import *


@ns.route('/')
class SampleList(Resource):
    @ns.doc(description='List all existing samples')
    @ns.marshal_list_with(sample_data, envelope='data')
    def get(self):
        return get_all_samples()

    @ns.doc(description='Save a new sample')
    @ns.response(201, 'Sample successfully created.')
    @ns.response(409, 'Sample with same id exists.')
    @ns.expect(sample_data, validate=True)
    def post(self):
        if save_new_sample(data=request.json) is not None:
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sample with same id exists',
            }
            return response_object, 409


@ns.route('/<int:sample_id>')
@ns.param('sample_id', 'The Sample identifier')
class Sample(Resource):
    @ns.doc(description='Get the contents of a sample')
    @ns.response(404, 'Sample not found.')
    @ns.marshal_with(sample_data)
    def get(self, sample_id):
        sample = get_a_sample(sample_id)
        if not sample:
            ns.abort(404, 'Sample with id {} does not exist.'.format(sample_id))
        else:
            return sample