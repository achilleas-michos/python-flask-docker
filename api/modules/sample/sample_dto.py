from flask_restplus import Namespace, fields


namespace = Namespace('sample', description='sample related operations')

sample_data = namespace.model('sample', {
    'id': fields.Integer(required=True, description='Sample id'),
    'content': fields.String(required=True, description='Sample content')
})