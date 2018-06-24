class Config:
    SECRET_KEY = "ball ball you, dont bb, show me the code"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:port/depora"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevConfig,
    prod=ProdConfig
)
