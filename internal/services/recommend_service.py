from internal.repositories.log_repo import get_logs_by_module
from internal.network.utils import create_recommend_learning_paths
from internal.repositories.content_repo import get_contents
from internal.repositories.recommend_repo import create_recommendation, get_recommendation


class RecommendService:

    @staticmethod
    def create_recommendation_path(group_id, module_list, policy="popularity"):
        no_exercise = sum([str(c['level3_id']) in module_list for c in get_contents()])
        logs = get_logs_by_module(module_list)
        # default paths that is not filtered by user cluster
        default_paths = create_recommend_learning_paths(logs, no_exercise, policy=policy)
        if default_paths:
            for index, path in enumerate(default_paths):
                create_recommendation(path[0], group_id, 5, policy, index + 1)

        for c in range(5):
            filtered_logs = list(filter(lambda x: x['cluster'] == c, logs))
            paths = create_recommend_learning_paths(filtered_logs, no_exercise, policy=policy)
            if paths:
                for index, path in enumerate(paths):
                    create_recommendation(path[0], group_id, c, policy, index + 1)

    @staticmethod
    def get_recommendation_path(group_id):
        return get_recommendation(group_id)

    @staticmethod
    def save_recommendation_path(group_id, paths, policy):
        pass
