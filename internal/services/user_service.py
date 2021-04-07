from internal.repositories.user_repo import get_users, get_user, get_all_users
from internal.repositories.computed_cache_repo import get_user_cache, create_user_cache, get_user_algorithm_cache
from internal.services.predict_service import PredictService


class UserService:

    @staticmethod
    def get_user(id):
        if not get_user_cache(id):
            create_user_cache(id)
        computed_cache = get_user_cache(id)
        user = get_user(id)
        user_algorithm_cache = get_user_algorithm_cache(id)
        user_bin = user_algorithm_cache['bin']
        user_cluster = user_algorithm_cache['cluster']
        if user_bin:
            html, _ = PredictService.explain_prediction(int(id), user_bin)
            return {**computed_cache, **user, 'html': html, 'bin': user_bin, 'cluster': user_cluster}
        else:
            return {**computed_cache, **user, 'cluster': user_cluster}

    @staticmethod
    def get_all_users():
        return get_all_users()

    @staticmethod
    def get_users(user_list):
        return get_users(user_list)
