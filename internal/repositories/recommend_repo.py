from internal.db.db import db_instance
from internal.repositories.models import parse, Path


def create_recommendation(path_seq, group_id, cluster, policy, rank):
    pic = 'e0309575@u.nus.edu'
    parsed = [f"({group_id}, {cluster}, {path}, {rank}, {index + 1}, '{policy}', '{pic}', NOW(), '{pic}', NOW())" for index, path in enumerate(path_seq)]
    values = ', '.join(parsed)
    query = f"""
    INSERT INTO 
    recommend_cache 
    (group_id, cluster, content_id, rank, position, policy, created_by, created_at, updated_by, updated_at)
    VALUES
    {values};
    """
    res = db_instance.exec_transaction(query)
    return res


def get_recommendation(group_id):
    res = db_instance.fetch_rows("SELECT * FROM recommend_cache WHERE group_id = %s AND deleted_at IS NULL", (group_id,))
    res = [parse(Path.fields, row) for row in res]
    return res


