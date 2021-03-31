from flask_restplus import fields
from internal.api.v1.v1 import api_v1

user_read = api_v1.model('user_read', {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
    'gender': fields.String(),
    'points': fields.String(),
    'badges_cnt': fields.String(),
    'first_login_date_TW': fields.String(),
    'user_grade': fields.String(),
    'user_city': fields.String(),
    'is_self_coach': fields.String(),
    'belongs_to_class_cnt': fields.String(),
    'has_class_cnt': fields.String(),
    'has_teacher_cnt': fields.String(),
    'has_student_cnt': fields.String()
})


user_statistics_read = api_v1.inherit('user_statistics_read', user_read, {
    'uuid': fields.String(),
    'problems_attempted': fields.String(),
    'exercises_attempted': fields.String(),
    'avg_time_per_exercise': fields.String(),
    'avg_accuracy': fields.String(),
    'no_upgrades': fields.String(),
    'no_downgrades': fields.String(),
    'avg_hint_per_attempt': fields.String(),
    'avg_time_btw_problem': fields.String(),
    'html': fields.String(),
})
