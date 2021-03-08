from internal.db.db import db_instance


def create_group_modules(group_id, module_list):
    pic = 'e0309575@u.nus.edu'
    parsed = [f"({group_id}, {module}, '{pic}', NOW(), '{pic}', NOW())" for module in module_list]
    values = ', '.join(parsed)
    query = f"""
    INSERT INTO 
    group_modules 
    (group_id, module_id, created_by, created_at, updated_by, updated_at)
    VALUES
    {values};
    """
    res = db_instance.exec_transaction(query)
    return res


def get_group_modules(group_id):
    res = db_instance.fetch_rows("SELECT uuid FROM group_modules WHERE group_id = %s AND deleted_at IS NULL", (group_id,))
    res = [row['module_id'] for row in res]
    return res
