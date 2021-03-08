from internal.repositories.user_repo import get_users, get_user, get_all_users
from internal.repositories.computed_cache_repo import get_user_cache, create_user_cache


class UserService:

    @staticmethod
    def get_user(id):
        if not get_user_cache(id):
            create_user_cache(id)
        cache = get_user_cache(id)
        user = get_user(id)
        return {**cache, **user}

    @staticmethod
    def get_all_users():
        return get_all_users()

    @staticmethod
    def get_users(user_list):
        return get_users(user_list)
