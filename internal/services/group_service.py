from internal.repositories.group_repo import create_group
from internal.services.cluster_service import ClusterService


class GroupService:

    @staticmethod
    def create_group(name, module_list, user_list):
        group_id = create_group(name)
        ClusterService.cluster(group_id, user_list, module_list)
        return True

