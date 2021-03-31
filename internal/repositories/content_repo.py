from internal.db.db import db_instance
from internal.repositories.models import Content, parse


def get_contents():
    res = db_instance.fetch_rows(f"SELECT * FROM contents WHERE deleted_at IS NULL")
    res = [parse(Content.fields, row) for row in res]
    return res
