import pandas as pd
import numpy as np
from internal.repositories.log_repo import get_logs_by_modules
from internal.repositories.user_repo import get_users
from internal.repositories.computed_cache_repo import get_users_cache
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans


class ClusterService:
    @staticmethod
    def cluster(group_id, user_list, module_list):
        logs = get_logs_by_modules(module_list)
        users = get_users(user_list)
        users_stats = get_users_cache(user_list)
        return
