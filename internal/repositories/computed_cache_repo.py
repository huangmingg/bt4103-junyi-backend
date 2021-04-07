from internal.db.db import db_instance
from internal.repositories.models import UserCache, GroupComputedStats, parse


def get_user_cache(id):
    res = db_instance.fetch_row("SELECT * FROM computed_cache WHERE uuid = %s AND deleted_at IS NULL", (id,))
    res = parse(UserCache.fields, res) if res else None
    return res


def get_users_cache():
    res = db_instance.fetch_rows("SELECT * FROM computed_cache WHERE deleted_at IS NULL")
    res = [parse(UserCache.fields, row) for row in res] if res else []
    return res


def get_users_cache(user_list):
    user_list = ', '.join([f"({i})" for i in user_list])
    res = db_instance.fetch_rows(f"SELECT * FROM computed_cache WHERE uuid in ({user_list}) AND deleted_at IS NULL")
    res = [parse(UserCache.fields, row) for row in res] if res else []
    return res


def get_group_average(user_list):
    user_list = ', '.join([f"({i})" for i in user_list])
    query = f"""
    SELECT 
    AVG(avg_accuracy) AS avg_accuracy, 
    AVG(exercises_attempted) AS avg_exercises_attempted, 
    AVG(problems_attempted) AS avg_problems_attempted
    FROM computed_cache WHERE uuid in ({user_list}) AND deleted_at IS NULL
    """
    res = db_instance.fetch_row(query)
    res = parse(GroupComputedStats.fields, res) if res else None
    return res


def filter_users_by_clusters(user_list, cluster_list):
    user_list = ', '.join([f"({i})" for i in user_list])
    cluster_list = ', '.join([f"({i})" for i in cluster_list])
    query = f"""
    SELECT
        *
    FROM
    computed_cache 
    LEFT JOIN
    algorithm_cache
    ON
    computed_cache.uuid = algorithm_cache.uuid
    WHERE 
    computed_cache.uuid IN ({user_list})
    AND
    algorithm_cache.cluster IN ({cluster_list}) 
    AND 
    computed_cache.deleted_at IS NULL
    """
    res = db_instance.fetch_rows(query)
    res = [parse(UserCache.fields, row) for row in res] if res else []
    return res


def get_users_bin(user_list, cluster):
    user_list = ', '.join([f"({i})" for i in user_list])
    query = f"""
    SELECT
        a.uuid, u.name, a.bin
    FROM
    users u
    LEFT JOIN
    algorithm_cache a
    ON 
    u.id = a.uuid
    WHERE
    a.uuid IN ({user_list})
    AND
    a.cluster = {cluster}
    AND
    u.deleted_at IS NULL
    """
    res = db_instance.fetch_rows(query)
    return res


# TO-DO
def create_user_cache(id):
    return


# TO-DO
def update_user_cache(id):
    return
