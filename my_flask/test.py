from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    a = request.args
    b = request.data
    c = request.form
    print(a,b,c,sep="\n")
    print(c.getlist("asd"))
    return "aa"

@app.route("/login")
def login():
    abort(404)
    return "hh"

@app.errorhandler(404)
def the_error(err):
    return "is oo %s" % err


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

