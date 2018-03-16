# 通用配置
class Config:
    MONGO_URI = 'mongodb://localhost:27017/depora'
    MONGO_USERNAME = 'arias',
    MONGO_PASSWORD = '123456'


# 生产环境配置
class ProdConfig(Config):
    pass


# 开发环境配置
class DevConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
