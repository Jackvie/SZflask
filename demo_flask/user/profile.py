from user import user_bp

@user_bp.route("/a")
def user_profile():
    return 'user_profile'
