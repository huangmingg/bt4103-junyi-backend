from flask import request
from flask_restplus import Resource
import logging
from internal.dto.users import user_read, user_statistics_read
from internal.api.v1.v1 import api_v1
from internal.services.user_service import UserService

logger = logging.getLogger(__name__)

ns = api_v1.namespace('user', description='Operations related to User.')


@ns.route('/<id>')
@ns.param('id', 'uuid')
class User(Resource):
    @ns.marshal_with(user_statistics_read)
    def get(self, id):
        res = UserService.get_user(id)
        return res


@ns.route('/')
class UserList(Resource):
    @ns.marshal_list_with(user_read)
    def get(self):
        res = UserService.get_users()
        return res
