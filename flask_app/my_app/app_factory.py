from flask import Blueprint, Flask

from flask_app.my_app.blueprints.my_app.urls import map_urls

my_app = Blueprint(
    'my_app',
    __name__,
    url_prefix='/my_app'
)

map_urls(my_app)

def initialize_app(config_class, blueprints=[my_app]):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app