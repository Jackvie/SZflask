from flask import Flask,request,abort,Response,redirect,url_for,render_template
import json, urllib.request
from werkzeug.routing import BaseConverter

app = Flask(__name__)

app.config.from_pyfile("config.cfg")
print(app.config.get("ITCAST"))


# @app.route("/")
@app.route("/", methods=["POST","GET"])
def index():
    print(request.method)
    return "OK"

@app.route("/hi2/<path:bid>")
@app.route("/hi/<path:bid>")
def hi(bid):
    return str((request.path,bid))

@app.route("/login")
def login():
    url = url_for("index")
    return redirect(url)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        print("__init__")
        self.regex = regex

    def to_python(self, value):
        print("to_python")
        return value
    
    def to_url(self, value):
        print("to_url")
        return value
app.url_map.converters["re"] = RegexConverter

@app.route("/opposite")
def opposite():
    print("opposite1")
    url = url_for("mobile", tel="12345678901")
    print("opposite2")
    return redirect(url)

@app.route("/mobile/<re(r'\d{11}'):tel>")
def mobile(tel):
    print("mobile")
    return tel

@app.route("/xss", methods=["GET","POST"])
def xss():
    return render_template("form.html")

if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0",port=5000)
