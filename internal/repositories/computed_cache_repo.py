from internal.db.db import db_instance
from internal.repositories.models import UserCache, parse


def get_user_cache(id):
    res = db_instance.fetch_row("SELECT * FROM computed_cache WHERE uuid = %s AND deleted_at IS NULL", (id,))
    res = parse(UserCache.fields, res)
    return res


def get_users_cache():
    res = db_instance.fetch_rows("SELECT * FROM computed_cache WHERE deleted_at IS NULL")
    res = [parse(UserCache.fields, row) for row in res]
    return res


def get_users_cache(user_list):
    user_list = ', '.join([f"({i})" for i in user_list])
    res = db_instance.fetch_rows(f"SELECT * FROM computed_cache WHERE uuid in ({user_list}) AND deleted_at IS NULL")
    res = [parse(UserCache.fields, row) for row in res]
    return res


# TO-DO
def create_user_cache(id):
    return


# TO-DO
def update_user_cache(id):
    return
