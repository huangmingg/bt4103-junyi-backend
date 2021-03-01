from flask import request
from flask_restplus import Resource
import logging
from internal.api.v1.v1 import api_v1
from internal.dto.groups import group_read, group_create

logger = logging.getLogger(__name__)

ns = api_v1.namespace('group', description='Operations related to group.')


@ns.route('/')
class Group(Resource):
    @ns.expect(group_create)
    @ns.marshal_with(group_create)
    def post(self):
        print(api_v1.payload)
        pass

    @ns.marshal_with(group_read)
    def get(self):
        pass


@ns.route('/<id>')
@ns.param('id', 'group_id')
class GroupList(Resource):
    @api_v1.marshal_with(group_create)
    def get(self):
        pass
