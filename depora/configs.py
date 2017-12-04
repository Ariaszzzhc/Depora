# 通用配置
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hancheng123@127.0.0.1:3306/depora_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# 生产环境配置
class ProdConfig(Config):
    pass


# 开发环境配置
class DevConfig(Config):
    DEBUG = True
