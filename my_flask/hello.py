from flask import Flask,jsonify, abort,redirect, url_for, request, make_response
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class Regex_url(BaseConverter):
    def __init__(self, url_map, *args):
        super().__init__(url_map)
        self.regex = args[0]
    
    def to_python(self, value):
        print("to_python")
        return value

    def to_url(self, value):
        print("to_url")
        return value

app.url_map.converters["re"] = Regex_url

@app.route("/setcookies")
def test_set_cookies():
    # res = make_response("result")
    res = jsonify(a=1,b=2)
    res.set_cookie("username", "itcas11t")
    #res.set_cookie("username", "itcast")
    return res
@app.route("/getcookies")
def test_get_cookies():
    res = request.cookies.get("username")
    return res


@app.route("/")
def login():
    url = url_for("index", num=10)
    #return redirect("/hello/1")
    print(url)
    return redirect(url)

@app.route("/hello/<int:num>")
def index(num):
    abort(404)
    return jsonify(code=1, num=num),200

@app.route("/register/<re('^1\d{10}$'):mobile>")
def register(mobile):
    return mobile
    
@app.errorhandler(404)
def handle_exceptions(e):
    return "error: {}"

if __name__ == "__main__":
    app.run(debug=True, host="192.168.118.130",port="5000")
