from internal.db.db import db_instance


def get_user_information(module_list, user_list):
    pass
    f"SELECT * FROM logs WHERE user in {user_list} AND"
    # pic = 'e0309575@u.nus.edu'
    # parsed = [f"({group_id}, {user}, '{pic}', NOW(), '{pic}', NOW())" for user in user_list]
    # values = ', '.join(parsed)
    # query = f"""
    # INSERT INTO
    # group_enrollments
    # (group_id, uuid, created_by, created_at, updated_by, updated_at)
    # VALUES
    # {values};
    # """
    # res = db_instance.exec_transaction(query)
    # return res