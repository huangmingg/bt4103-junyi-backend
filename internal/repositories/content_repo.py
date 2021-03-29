from internal.db.db import db_instance


def get_contents():
    res = db_instance.fetch_rows(f"SELECT * FROM contents WHERE deleted_at IS NULL")
    return res
