from internal.repositories.group_repo import create_group, get_groups
from internal.repositories.group_enrollment_repo import create_enrollments, get_enrollments
from internal.repositories.group_modules_repo import create_group_modules
from internal.repositories.user_repo import get_users
from internal.services.recommend_service import RecommendService
from internal.repositories.computed_cache_repo import get_group_average, filter_users_by_clusters, get_users_bin
import logging

logger = logging.getLogger(__name__)


class GroupService:

    @staticmethod
    def create_group(name, module_list, user_list):
        group_id = create_group(name)
        enrollment_creation = create_enrollments(group_id, user_list)
        module_creation = create_group_modules(group_id, module_list)
        if enrollment_creation and module_creation:
            RecommendService.create_recommendation_path(group_id, module_list)
            return True
        else:
            return False

    @staticmethod
    def get_groups():
        groups = get_groups()
        stats = [{**get_group_average(get_enrollments(group['id'])), 'no_students': len(get_enrollments(group['id']))} for group in groups]
        res = [{**groups[i], **stats[i]} for i in range(len(groups))]
        return res

    @staticmethod
    def get_group_users(group_id):
        user_id = get_enrollments(group_id)
        res = get_users(user_id)
        return res

    @staticmethod
    def get_group_paths(group_id, cluster):
        user_list = get_enrollments(group_id)
        paths = RecommendService.get_recommendation_path(group_id, cluster)
        users = filter_users_by_clusters(user_list, [cluster])
        if not users:
            logger.info("No students in this cluster")
            return None
        else:
            stats = {**get_group_average([user['uuid'] for user in users]), 'no_students': len(users)}
            predictions = get_users_bin(user_list, cluster)
            output = {**stats, 'paths': paths, 'predictions': predictions}
            return output
