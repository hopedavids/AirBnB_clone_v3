#!/usr/bin/python
""" define the url route to check the status for the app """

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def get_status():
    """ Define the route """
    return jsonify({"status": "OK"})

