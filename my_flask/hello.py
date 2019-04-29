from flask import *
from werkzeug.routing import BaseConverter

# 设置根目录
app = Flask(__name__,
            static_url_path = "/s",
            static_folder = "static",
            template_folder = "templates",
        )

class Config(object):
    # 类属性
    DEBUG = True
    NAME = "Jackvie"

app.config.from_object(Config)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex
        print(self.__dir__)
        print(self.__dict__)
        print(RegexConverter.__mro__)

app.url_map.converters["a"] = RegexConverter

@app.route("""/index/<a(r"1\d{10}"):bid>""")
def index(bid):
    print(type(bid))
    c = BaseConverter(app.url_map)
    print(c.__dict__)
    b = "bb%sbb" % bid
    a = current_app.config.get("NAME")
    return b


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
