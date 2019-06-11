import redis

class Config(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "sadirwkrldf"

    # mysql
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # session
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400

class DevelopmentConfig(Config):
    """开发"""
    DEBUG = True


class ProductConfig(Config):
    """生产"""
    DEBUG = False
    pass

config_map = {
            "develop": DevelopmentConfig,
            "product": ProductConfig
        }
