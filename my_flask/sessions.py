from flask import Flask,request,session
from flask_script import Manager

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdasfjasjf"

manager = Manager(app)

@app.before_first_request
def before():
    print("before")

@app.before_request
def first():
    print("first")
@app.after_request
def after(response):
    print("after")
    return response

@app.teardown_request
def teardown(response):
    print("teardown")
    return response

@app.route("/")
def index():
    print(request.args)
    a = 1/0
    a = request.args.get("aa")
    session["b"] = 123
    return "haha %s" % a
@app.route("/b")
def b():
    b = session.get("b")
    return "session %s" % b

if __name__ == "__main__":
    # app.run(debug=False, host="0.0.0.0", port="5000")
    manager.run()

