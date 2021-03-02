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


user_statistics_read = api_v1.inherit('user_statistics_read', user_read, {
    'uuid': fields.Integer(),
    'problems_attempted': fields.Integer(),
    'exercises_attempted': fields.Integer(),
    'avg_time_per_exercise': fields.Decimal(),
    'avg_accuracy': fields.Decimal(),
    'no_upgrades': fields.Integer(),
    'no_downgrades': fields.Integer(),
    'avg_hint_per_attempt': fields.Decimal(),
    'avg_time_btw_problem': fields.Decimal(),
})
