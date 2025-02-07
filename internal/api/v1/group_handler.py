from flask import request
from flask_restplus import Resource
import logging
from internal.api.v1.v1 import api_v1
from internal.dto.groups import group_read, group_create
from internal.dto.users import user_read
from internal.dto.paths import group_cluster_read
from internal.services.group_service import GroupService
logger = logging.getLogger(__name__)

ns = api_v1.namespace('group', description='Operations related to group.')


@ns.route('/')
class Group(Resource):
    @ns.expect(group_create)
    @api_v1.marshal_with(group_create)
    def post(self):
        body = request.get_json()
        if (not body['modules']) or (not body['users']) or (not body['name']):
            logger.info("Missing parameters from request")
        else:
            GroupService.create_group(body['name'], body['modules'], body['users'])
            return {'name': f"Group {body['name']} successfully created"}

    @api_v1.marshal_list_with(group_read)
    def get(self):
        res = GroupService.get_groups()
        return res


@ns.route('/<id>/students')
@ns.param('id', 'group_id')
class GroupStudent(Resource):
    @api_v1.marshal_with(user_read)
    def get(self, id):
        return GroupService.get_group_users(id)


@ns.route('/<group_id>/cluster/<cluster_no>')
@ns.param('group_id', 'group_id')
@ns.param('cluster_no', 'cluster_no')
class GroupCluster(Resource):
    @api_v1.marshal_list_with(group_cluster_read)
    def get(self, group_id, cluster_no):
        res = GroupService.get_group_paths(group_id, cluster_no)
        if res:
            return {**res, 'group_id': group_id, 'cluster': cluster_no}
        else:
            return {'group_id': group_id, 'cluster': cluster_no}
