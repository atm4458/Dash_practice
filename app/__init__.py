from flask import Flask
from flask.helpers import get_root_path
from flask_bootstrap import Bootstrap5
from app.index import base_app
from dash import Dash
import dash_bootstrap_components as dbc

from config import Config


def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)
    bootstrap = Bootstrap5(server)

    register_flask_app(server)
    register_dash_app(server)

    return server


def register_flask_app(server):
    server.register_blueprint(base_app)


def register_dash_app(server):
    from app.dash_app import layout

    dash_app = Dash(__name__,
                    server=server,
                    use_pages=True,
                    url_base_pathname='/dashboard/',
                    pages_folder=get_root_path(__name__) + '/dash_app/pages/',
                    assets_folder=get_root_path(__name__) + '/dashboard/assets/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP])

    with server.app_context():
        dash_app.title = "Dash App"
        dash_app.layout = layout
