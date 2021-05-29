from flask_app.my_app.app_factory import initialize_app
from flask_app.my_app.config import ConfigClass

app = initialize_app(ConfigClass)