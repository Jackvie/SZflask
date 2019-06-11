from flask import Flask
from user import user_bp
from admin import admin_bp

app = Flask(__name__)

app.register_blueprint(user_bp,url_prefix='/user')
app.register_blueprint(admin_bp, url_prefix='/admin')

print(app.url_map)
app.run()
