from flask_restful import Api

from flask_app.my_app.blueprints.my_app.controllers.status import StatusController

def map_urls(blueprint):
    api = Api(blueprint)

    api.add_resource(
        StatusController,
        '/status',
        endpoint="status"
    )