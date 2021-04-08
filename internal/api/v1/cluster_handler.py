from flask_restplus import Resource
from flask import request
import logging
from internal.dto.clusters import cluster_read, cluster_update
from internal.api.v1.v1 import api_v1
from internal.services.cluster_service import ClusterService

logger = logging.getLogger(__name__)

ns = api_v1.namespace('cluster', description='Operations related to Cluster.')


@ns.route('/<id>')
@ns.param('id', 'cluster_id')
class Cluster(Resource):
    @ns.expect(cluster_update)
    @api_v1.marshal_with(cluster_update)
    def put(self, id):
        body = request.get_json()
        if (body['name']) and (body['description']):
            res = ClusterService.update_cluster(id, body['name'], body['description'])
            return res
        else:
            logger.info("Missing parameters from request")


@ns.route('/')
class ClusterList(Resource):
    @ns.marshal_list_with(cluster_read)
    def get(self):
        res = ClusterService.get_clusters()
        return res
