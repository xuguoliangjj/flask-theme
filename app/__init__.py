# -*- coding: utf-8 -*-
from flask import Flask
from config import config

app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .routes import main
    from .routes import news
    app.register_blueprint(main.bp, url_prefix='/')
    app.register_blueprint(news.bp, url_prefix='/news')

    return app