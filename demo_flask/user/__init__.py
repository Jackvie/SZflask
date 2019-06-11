from flask import Blueprint


user_bp = Blueprint('user', __name__)
from user.profile import user_profile
