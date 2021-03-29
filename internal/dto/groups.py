from flask_restplus import fields
from internal.api.v1.v1 import api_v1

group_create = api_v1.model('group_create', {
    'name': fields.String(required=True),
    'modules': fields.List(fields.String()),
    'users': fields.List(fields.String()),
})

group_read = api_v1.model('group_read', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'no_students': fields.String(required=True),
    'avg_accuracy': fields.String(required=True),
    'avg_exercises_attempted': fields.String(required=True),
    'avg_problems_attempted': fields.String(required=True),
})

