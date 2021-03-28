from internal.repositories.group_repo import create_group, get_groups
from internal.repositories.group_enrollment_repo import create_enrollments, get_enrollments
from internal.repositories.group_modules_repo import create_group_modules
from internal.repositories.user_repo import get_users
from internal.services.recommend_service import RecommendService


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
        return get_groups()

    @staticmethod
    def get_group_users(group_id):
        user_id = get_enrollments(group_id)
        res = get_users(user_id)
        return res

    @staticmethod
    def get_group_paths(group_id):
        return RecommendService.get_recommendation_path(group_id)
