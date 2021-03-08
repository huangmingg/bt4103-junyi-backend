from flask_restful_swagger import swagger
import logging
from flask_restplus import Api

log = logging.getLogger(__name__)

api_v1 = swagger.docs(Api(
    version="1.0",
    title="Monolithic Service",
    validate=True,
))

generic_arguments = api_v1.parser()
generic_arguments.add_argument(
    "username",
    type=str,
    required=False,
    location="headers",
)


@api_v1.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred, please check the logs for more information."
    log.exception(message, e)
    return {"message": message}, 500

