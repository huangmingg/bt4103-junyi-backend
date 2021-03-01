from flask_restplus import fields
from internal.api.v1.v1 import api_v1

user_read = api_v1.model('user_read', {
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


user_statistics = api_v1.inherit('user_statistics', user_read, {
    'average_time': fields.String(),
    'average_problem_length': fields.Decimal()
})
