from flask import request
from flask_restplus import Resource
import logging
from internal.api.v1.v1 import api_v1
from internal.dto.groups import group_read, group_create
from internal.dto.users import user_read
from internal.services.group_service import GroupService
logger = logging.getLogger(__name__)

ns = api_v1.namespace('group', description='Operations related to group.')


@ns.route('/')
class Group(Resource):
    @ns.expect(group_create)
    @ns.marshal_with(group_create)
    def post(self):
        body = request.get_json()
        GroupService.create_group(body['name'], body['modules'], body['users'])

    @ns.marshal_list_with(group_read)
    def get(self):
        res = GroupService.get_groups()
        return res


@ns.route('/<id>/students')
@ns.param('id', 'group_id')
class GroupStudent(Resource):
    @api_v1.marshal_with(user_read)
    def get(self, id):
        return GroupService.get_group_users(id)
