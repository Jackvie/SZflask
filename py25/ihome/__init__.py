from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis


# mysql
db = SQLAlchemy()
# redis 
redis_store = None

# 工厂模式
def create_app(config_name):
    """创建app"""

    app = Flask(__name__)
    #config
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    # mysql
    db.init_app(app)
    # redis
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST,port=config_class.REDIS_PORT)
    # session
    Session(app)
    # csrftoken
    CSRFProtect(app)

    from ihome import apibp
    app.register_blueprint(apibp.api, url_prefix='/api/v1.0')

    return app
