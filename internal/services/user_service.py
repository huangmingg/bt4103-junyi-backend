from internal.repositories.user_repo import get_users, get_user
from internal.repositories.computed_cache import get_user_cache, create_user_cache


class UserService:

    @staticmethod
    def get_user(id):
        if not get_user_cache(id):
            create_user_cache(id)
        cache = get_user_cache()
        user = get_user(id)
        return {**cache, **user}

    @staticmethod
    def get_users():
        return get_users()
