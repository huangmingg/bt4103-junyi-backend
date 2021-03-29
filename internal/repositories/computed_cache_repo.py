from internal.db.db import db_instance
from internal.repositories.models import UserCache, GroupComputedStats, parse


def get_user_cache(id):
    res = db_instance.fetch_row("SELECT * FROM computed_cache WHERE uuid = %s AND deleted_at IS NULL", (id,))
    res = parse(UserCache.fields, res)
    return res


def get_users_cache():
    res = db_instance.fetch_rows("SELECT * FROM computed_cache WHERE deleted_at IS NULL")
    res = [parse(UserCache.fields, row) for row in res]
    return res


def get_users_cache(user_list):
    user_list = ', '.join([f"({i})" for i in user_list])
    res = db_instance.fetch_rows(f"SELECT * FROM computed_cache WHERE uuid in ({user_list}) AND deleted_at IS NULL")
    res = [parse(UserCache.fields, row) for row in res]
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
    res = parse(GroupComputedStats.fields, res)
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
    cluster_cache
    ON
    computed_cache.uuid = cluster_cache.uuid
    WHERE 
    computed_cache.uuid IN ({user_list})
    AND
    cluster_cache.cluster IN ({cluster_list}) 
    AND 
    computed_cache.deleted_at IS NULL
    """
    res = db_instance.fetch_rows(query)
    res = [parse(UserCache.fields, row) for row in res]
    return res


# TO-DO
def create_user_cache(id):
    return


# TO-DO
def update_user_cache(id):
    return
