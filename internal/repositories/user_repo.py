from internal.db.db import db_instance
from internal.repositories.models import User, parse


def get_user(id):
    res = db_instance.fetch_row("SELECT * FROM users WHERE id = %s AND deleted_at IS NULL", (id,))
    res = parse(User.fields, res)
    return res


def get_all_users():
    query = "SELECT * FROM users WHERE deleted_at IS NULL"
    res = db_instance.fetch_rows(query)
    res = [parse(User.fields, row) for row in res]
    return res


def get_users(user_list):
    user_list = ', '.join([f"({i})" for i in user_list])
    query = f"SELECT * FROM users WHERE id in ({user_list}) AND deleted_at IS NULL"
    res = db_instance.fetch_rows(query)
    res = [parse(User.fields, row) for row in res]
    return res
