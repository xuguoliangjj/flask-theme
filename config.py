# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    @staticmethod
    def init_app(app):
        pass


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/testdb"

# 生产环境的配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/testdb"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}