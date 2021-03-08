from internal.db.db import db_instance


def create_enrollments(group_id, user_list):
    pic = 'e0309575@u.nus.edu'
    parsed = [f"({group_id}, {user}, '{pic}', NOW(), '{pic}', NOW())" for user in user_list]
    values = ', '.join(parsed)
    query = f"""
    INSERT INTO 
    group_enrollments 
    (group_id, uuid, created_by, created_at, updated_by, updated_at)
    VALUES
    {values};
    """
    res = db_instance.exec_transaction(query)
    return res


def get_enrollments(group_id):
    res = db_instance.fetch_rows("SELECT uuid FROM group_enrollments WHERE group_id = %s AND deleted_at IS NULL", (group_id,))
    res = [row['uuid'] for row in res]
    return res
