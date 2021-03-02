from flask_restplus import fields
from internal.api.v1.v1 import api_v1

group_create = api_v1.model('group_create', {
    'name': fields.String(required=True),
    'modules': fields.List(fields.Integer()),
    'users': fields.List(fields.Integer()),
})

group_read = api_v1.model('group_read', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
})

