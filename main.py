from flask import Flask, Blueprint
from flask_cors import CORS
from internal.api.v1.v1 import api_v1
from internal.api.v1.user_handler import ns as user_ns
from internal.api.v1.group_handler import ns as group_ns
from internal.api.v1.cluster_handler import ns as cluster_ns
from internal.db.db import db_instance
from internal.migration.migration import migrate_database
import os
import logging

logging.basicConfig(level=logging.INFO)
app_directory = os.getcwd()


def main():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, resources={r"/v1/*": {"origins": "*"}})

    migrate_database(db_instance, os.path.join(app_directory, "migration"))
    setup_routing(app)
    app.run(port=8081)


def setup_routing(app):
    blueprint = Blueprint('v1', __name__, url_prefix='/v1')
    api_v1.init_app(blueprint)
    api_v1.add_namespace(user_ns)
    api_v1.add_namespace(group_ns)
    api_v1.add_namespace(cluster_ns)
    app.register_blueprint(blueprint)


def clean_up():
    pass


if __name__ == "__main__":
    main()
