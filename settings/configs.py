
"""
URI FORMAT

postgresql://user:passsword@127.0.0.1:5432/databasename

"""
class BaseConfig:
    SECRET_KEY = "sdfsdafasdfsad"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """"configs for the dev env"""
    ENV="development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:wamzy@127.0.0.1:5432/septemberdb" 

class ProductionConfig(BaseConfig):
    """configs for production"""
    pass
    