from xgboost import XGBClassifier
import os
import shap
import logging

logger = logging.getLogger(__name__)

MODEL_DIRECTORY = os.path.join(os.getcwd(), "client")


def get_shap_values(feature):
    xgb_clf = XGBClassifier()
    xgb_clf.load_model(os.path.join(MODEL_DIRECTORY, "xgb.model"))
    explainer = shap.TreeExplainer(xgb_clf)
    values = explainer.shap_values(feature)
    return values


def generate_shap_html(feature, user_bin, user_id):
    xgb_clf = XGBClassifier()
    xgb_clf.load_model(os.path.join(MODEL_DIRECTORY, "xgb.model"))
    explainer = shap.TreeExplainer(xgb_clf)
    values = explainer.shap_values(feature)
    shap.initjs()
    fp = shap.force_plot(explainer.expected_value[user_bin - 1], values[user_bin - 1][0], feature, show=False)

    shap.save_html(os.path.join(MODEL_DIRECTORY, f"User_{user_id}.html"), fp)
    with open(os.path.join(MODEL_DIRECTORY, f"User_{user_id}.html"), "r", encoding='utf-8') as f:
        html = f.read()
    os.remove(os.path.join(MODEL_DIRECTORY, f"User_{user_id}.html"))
    return str(html), values
