from client.aws import get_shap_values, generate_shap_html
from internal.repositories.user_repo import get_user
from internal.repositories.log_repo import get_logs_by_user
from internal.repositories.content_repo import get_contents
import pandas as pd
import numpy as np


class PredictService:

    @staticmethod
    def predict_performance(user_id):
        pass

    # Modified from https://github.com/timmmlim/bt4103-junyi
    @staticmethod
    def explain_prediction(user_id, user_bin):
        logs = get_logs_by_user([user_id])
        user = get_user(user_id)
        logs = pd.DataFrame(logs)
        logs = logs.sort_values(by=['attempt_timestamp', 'ucid', 'problem_number'])
        contents = get_contents()
        contents = pd.DataFrame(contents)
        df = pd.merge(logs, contents[['id', 'difficulty', 'learning_stage']], how='left', left_on='ucid', right_on='id')
        n_ucid = len(df['ucid'].unique())
        n_repeated_upid = sum(df['upid'].value_counts() > 1)
        curr_avg_acc = len(df.loc[df['is_correct'] == 'True']) / len(df)
        avg_sec_taken = np.mean(df['total_sec_taken'].to_numpy(dtype=np.int64))
        n_upgrades = len(df.loc[df['is_upgrade'] == 'True'])
        n_downgrades = len(df.loc[df['is_downgrade'] == 'True'])
        ls_counts = df['learning_stage'].value_counts()
        n_elementary = _get_ls_counts(ls_counts, 'elementary')
        n_junior = _get_ls_counts(ls_counts, 'junior')
        n_senior = _get_ls_counts(ls_counts, 'senior')
        user_grade = int(user['user_grade'])
        user_self_coach = bool(user['is_self_coach'])
        user_dict = {
            'n_ucid': [n_ucid],
            'n_repeated_upid': [n_repeated_upid],
            'curr_avg_acc': [curr_avg_acc],
            'avg_sec_taken': [avg_sec_taken],
            'n_upgrades': [n_upgrades],
            'n_downgrades': [n_downgrades],
            'n_elementary': [n_elementary],
            'n_junior': [n_junior],
            'n_senior': [n_senior],
            'user_grade': [user_grade],
            'user_self_coach': [user_self_coach]
        }
        feature = pd.DataFrame(user_dict)
        html, values = generate_shap_html(feature, user_bin, user_id)
        return html, values


def _get_ls_counts(value_counts, ls):
    try:
        counts = value_counts.loc[ls]
    except KeyError:
        counts = 0
    return counts
