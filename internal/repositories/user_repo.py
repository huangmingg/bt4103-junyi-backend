from internal.db.db import db_instance
import logging


def get_user(id):
    res = db_instance.fetch_row("SELECT * FROM users WHERE id = %s", (id,))
    return res


def get_users():
    query = "SELECT * FROM users"
    res = db_instance.fetch_rows(query)
    return res
