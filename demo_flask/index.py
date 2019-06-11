from flask import Flask, current_app,jsonify


def create_flask_config(config):
    """config"""
    app = Flask(__name__)
    app.config.from_object(config)
    
    return app

class DefaultConfig(object):
    """默认配置"""
    SECRET_KEY = "qwertyuiop"
    DEBUG = True

app = create_flask_config(DefaultConfig)


@app.route("/")
def index():
    return current_app.config.get("SECRET_KEY"),"999 ITCAST",[("HA","HAHA")]

@app.route("/route_map", methods=["POST","GET"])
def route_map():
    """"""
    rules_iterator = app.url_map.iter_rules()
    return jsonify(**{rule.endpoint:rule.rule for rule in rules_iterator})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    """"""
