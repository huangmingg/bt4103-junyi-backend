from internal.db.db import db_instance
import logging

def get_user(id):
    logging.info(id)
    params = (id,)
    res = db_instance.fetch_row("SELECT * FROM users WHERE id = %s", params)
    print("pepe")
    logging.info("pepe")
    logging.info(res)
    print(res)
    return res


def get_users():
    query = "SELECT * FROM users LIMIT 5"
    res = db_instance.fetch_rows(query)
    return res