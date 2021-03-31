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

user_bin = api_v1.model('user_bin', {
    'uuid': fields.String(required=True),
    'name': fields.String(required=True),
    'bin': fields.String(required=True)
})

group_cluster_read = api_v1.model('group_cluster_read', {
    'no_students': fields.String(required=True),
    'avg_accuracy': fields.String(required=True),
    'avg_exercises_attempted': fields.String(required=True),
    'avg_problems_attempted': fields.String(required=True),
    'predictions': fields.List(fields.Nested(user_bin)),
    'paths': fields.List(fields.Nested(path_read)),
})

