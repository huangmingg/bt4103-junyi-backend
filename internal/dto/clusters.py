from flask_restplus import fields
from internal.api.v1.v1 import api_v1

cluster_read = api_v1.model('cluster_read', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'description': fields.String(required=True),
})

cluster_update = api_v1.model('cluster_update', {
    'name': fields.String(required=True),
    'description': fields.String(required=True),
})
