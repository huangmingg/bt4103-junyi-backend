import os
import json

app_path = os.environ.get("BACKEND_PATH")


def get_env_config(path=None):
    if not path and not app_path:
        path = os.path.join(os.getcwd(), 'config', 'default.json')
    elif not path:
        path = os.path.join(app_path, 'config', 'default.json')
    with open(path, 'r') as config_file:
        config_data = json.loads(config_file.read())
    config_file.close()
    return config_data


def set_app_path(path):
    global app_path
    app_path = path


def get_app_path():
    return app_path
