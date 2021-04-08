from internal.repositories.cluster_repo import get_clusters, update_cluster


class ClusterService:

    @staticmethod
    def get_clusters():
        return get_clusters()


    @staticmethod
    def update_cluster(id, new_name, new_description):
        return update_cluster(id, new_name, new_description)
