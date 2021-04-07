from internal.repositories.log_repo import get_logs_by_module
from internal.network.utils import create_recommend_learning_paths
from internal.repositories.recommend_repo import create_recommendation, get_recommendation


class RecommendService:

    @staticmethod
    def create_recommendation_path(group_id, module_list, methods=["number_of_individual_students", "final_average_performance", "shortest_path"]):
        logs = get_logs_by_module(module_list)
        for cluster in range(5):
            filtered_logs = list(filter(lambda x: x['cluster'] == cluster, logs))
            for method in methods:
                paths = create_recommend_learning_paths(filtered_logs, method=method)
                if paths:
                    for index, path in enumerate(paths):
                        create_recommendation(path, group_id, cluster, method, index + 1)

    @staticmethod
    def get_recommendation_path(group_id):
        return get_recommendation(group_id)

    @staticmethod
    def save_recommendation_path(group_id, paths, policy):
        pass
