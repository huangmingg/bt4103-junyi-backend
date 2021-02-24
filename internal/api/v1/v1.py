from flask_restful_swagger import swagger
import logging
from flask_restplus import Api, fields

log = logging.getLogger(__name__)

api_v1 = swagger.docs(Api(
    version="1.0",
    title="Monolithic Service",
    validate=True,
))

generic_arguments = api_v1.parser()
generic_arguments.add_argument(
    "username",
    type=str,
    required=False,
    location="headers",
)


@api_v1.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred, please check the logs for more information."
    log.exception(message, e)
    return {"message": message}, 500


basic_response = api_v1.model('basic', {
    'response_code': fields.String(required=True),
    'message': fields.String()
})


user = api_v1.model('user', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'gender': fields.String(),
    'points': fields.Integer(),
    'badges_cnt': fields.Integer(),
    'first_login_date_TW': fields.Date(),
    'user_grade': fields.Integer(),
    'user_city': fields.String(),
    'is_self_coach': fields.Boolean(),
    'belongs_to_class_cnt': fields.Integer(),
    'has_class_cnt': fields.Integer(),
    'has_teacher_cnt': fields.Integer(),
    'has_student_cnt': fields.Integer()
})

