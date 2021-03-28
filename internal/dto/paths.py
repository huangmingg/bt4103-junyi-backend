from flask_restplus import fields
from internal.api.v1.v1 import api_v1

path_read = api_v1.model('path_read', {
    'id': fields.String(required=True),
    'group_id': fields.String(required=True),
    'cluster': fields.String(required=True),
    'content_id': fields.String(required=True),
    'rank': fields.String(required=True),
    'position': fields.String(required=True),
    'policy': fields.String(required=True)
})
