from internal.db.db import db_instance


def get_user(id):
    res = db_instance.fetch_row("SELECT * FROM users WHERE id = %s AND deleted_at IS NULL", (id,))
    return res


def get_users():
    query = "SELECT * FROM users WHERE deleted_at IS NULL"
    res = db_instance.fetch_rows(query)
    return res
