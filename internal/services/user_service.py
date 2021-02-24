from internal.repositories.user_repo import get_users, get_user


class UserService:

    @staticmethod
    def get_user(id):
        return get_user(id)

    @staticmethod
    def get_users():
        return get_users()
