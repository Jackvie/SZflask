from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import pymysql, redis

app = Flask(__name__)

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

#config
app.config.from_object(Config)
# mysql
db = SQLAlchemy(app)
# redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# session
Session(app)
# csrf
CSRFProtect(app)


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    pymysql.install_as_MySQLdb()
    app.run()
