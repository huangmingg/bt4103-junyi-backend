from flask import request
from flask_restplus import Resource

import logging
from internal.api.v1.v1 import api_v1, user
from internal.services.user_service import UserService

log = logging.getLogger(__name__)

ns = api_v1.namespace('user', description='Operations related to User.')


@ns.route('/<id>')
@ns.param('id', 'uuid')
class User(Resource):
    @api_v1.marshal_with(user)
    def get(self, id):
        # print(id)
        res = UserService.get_user("ylShf5uYmmFFypbU/LZPX8xdhHnp8a94GgvQi8jmUzg=")
        return res


@ns.route('/')
class UserList(Resource):
    @api_v1.marshal_with(user)
    def get(self):
        res = UserService.get_users()
        return res
