from internal.db.db import db_instance


def get_user_cache(id):
    res = db_instance.fetch_row("SELECT * FROM computed_cache WHERE uuid = %s AND deleted_at IS NULL", (id,))
    return res


def get_users_cache():
    res = db_instance.fetch_rows("SELECT * FROM computed_cache WHERE deleted_at IS NULL")
    return res


# TO-DO
def create_user_cache(id):
    return


# TO-DO
def update_user_cache(id):
    return
