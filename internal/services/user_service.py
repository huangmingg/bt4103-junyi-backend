from internal.repositories.user_repo import get_users, get_user, get_all_users
from internal.repositories.computed_cache_repo import get_user_cache, create_user_cache, get_users_bin
from internal.services.predict_service import PredictService


class UserService:

    @staticmethod
    def get_user(id):
        if not get_user_cache(id):
            create_user_cache(id)
        computed_cache = get_user_cache(id)
        user = get_user(id)
        user_bin = get_users_bin([id])[0]['bin']
        if user_bin:
            html, _ = PredictService.explain_prediction(int(id), user_bin)
            return {**computed_cache, **user, 'html': html}
        else:
            return {**computed_cache, **user}

    @staticmethod
    def get_all_users():
        return get_all_users()

    @staticmethod
    def get_users(user_list):
        return get_users(user_list)
