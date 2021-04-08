from internal.db.db import db_instance
from internal.repositories.models import parse, Cluster


def get_clusters():
    res = db_instance.fetch_rows(f"SELECT * FROM clusters WHERE deleted_at IS NULL")
    res = [parse(Cluster.fields, row) for row in res]
    return res


def update_cluster(cluster_id, new_name, new_description):
    cluster_id = int(cluster_id)
    query = f"""
        UPDATE 
            clusters
        SET
            name = '{new_name}'
            , description = '{new_description}'
        WHERE
            id = {cluster_id};
        """
    res = db_instance.exec_transaction(query)
    return res
