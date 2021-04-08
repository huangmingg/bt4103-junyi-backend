def parse(fields, raw):
    output = {}
    for i in fields:
        output[i] = str(raw[i])
    return output


class Model:
    fields = ['id', 'created_at', 'updated_at', 'deleted_at', 'created_by', 'updated_by', 'deleted_by']


class Content:
    fields = ['id', 'name', 'difficulty', 'learning_stage', 'level2_id', 'level3_id', 'level4_id']


class User:
    fields = ['id',
              'name',
              'gender',
              'points',
              'badges_cnt',
              'first_login_date_TW',
              'user_grade',
              'user_city',
              'is_self_coach',
              'belongs_to_class_cnt',
              'has_class_cnt',
              'has_teacher_cnt',
              'has_student_cnt']


class UserCache:
    fields = ['uuid',
              'problems_attempted',
              'exercises_attempted',
              'avg_time_per_exercise',
              'avg_accuracy',
              'no_downgrades',
              'no_upgrades',
              'avg_hint_per_attempt',
              'avg_time_btw_problem'
              ]


class Group:
    fields = ['id', 'name']


class GroupComputedStats:
    fields = ['avg_accuracy', 'avg_exercises_attempted', 'avg_problems_attempted']


class Path:
    fields = ['id', 'group_id', 'cluster', 'content_id', 'rank', 'position', 'policy']


class Log:
    fields = ['id',
              'upid',
              'uuid',
              'ucid',
              'attempt_timestamp',
              'problem_number',
              'exercise_problem_repeat_session',
              'is_correct',
              'total_sec_taken',
              'total_attempt_cnt',
              'used_hint_cnt',
              'is_hint_used',
              'is_downgrade',
              'is_upgrade',
              'user_level'
              ]


class Cluster:
    fields = ['id', 'name', 'description']