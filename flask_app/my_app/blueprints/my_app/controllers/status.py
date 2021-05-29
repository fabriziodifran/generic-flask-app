from flask.views import MethodView
from flask import current_app, jsonify

from flask_app.my_app import config

class StatusController(MethodView):
    """MethodView for Stock status controller."""

    def get(self):
        """Check api status.

        Returns
        -------
        Response
            api version and deploy information.
        """
        return jsonify({
            'api': current_app.config.get("API_NAME"),
            'version': config.API_VERSION
        })