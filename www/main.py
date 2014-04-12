#!/usr/bin/python
"""
API bootstrap file
"""
from flask import Flask
import argparse

def create_app():
    """ dynamically create the app """
    app = Flask(__name__, static_url_path='/static', static_folder='./static')
    app.config.from_object(__name__)
    from core.views import core
    app.register_blueprint(core, url_prefix="/")
    return app


def bootstrap(**kwargs):
    """bootstraps the application. can handle setup here"""
    app = create_app()
    app.debug = True
    app.run(host=kwargs['host'], port=kwargs['port'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Hostname or IP address",
        dest="host", type=str, default='0.0.0.0')
    parser.add_argument("--port", help="Port number",
        dest="port", type=int, default=8080)
    kwargs = parser.parse_args()
    bootstrap(**kwargs.__dict__)
