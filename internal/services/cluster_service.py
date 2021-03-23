import pandas as pd
import numpy as np
from internal.repositories.log_repo import get_logs_by_modules
from internal.repositories.user_repo import get_users
from internal.repositories.computed_cache_repo import get_users_cache
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans

CLUSTERING_COLUMNS = [
    'problems_attempted'
    , 'exercises_attempted'
    , 'avg_time_per_exercise'
    , 'avg_accuracy'
    , 'no_downgrades'
    , 'no_upgrades'
    , 'avg_hint_per_attempt'
    , 'avg_time_btw_problem'
    , 'points'
    , 'badges_cnt'
    , 'user_grade'
    , 'has_teacher_cnt'
    , 'has_student_cnt'
    , 'has_class_cnt'
    , 'belongs_to_class_cnt'
]


def scale_data(data, scaler):
    scaled_data = pd.DataFrame(scaler.fit_transform(data[data.columns]))
    scaled_data.columns = data.columns
    return scaled_data


class ClusterService:

    @staticmethod
    def cluster(group_id, user_list, module_list):
        logs = get_logs_by_modules(module_list)
        users_stats = pd.DataFrame(get_users_cache(user_list))
        users = pd.DataFrame(get_users(user_list)).join(users_stats.set_index('uuid'), on='id')
        users = users[CLUSTERING_COLUMNS]
        scaler = MinMaxScaler()
        scaled_clustering_input = scale_data(users, scaler)
        print(scaled_clustering_input)
        return









