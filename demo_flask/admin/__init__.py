from flask import Blueprint

admin_bp = Blueprint('admin',
            __name__,
            static_folder='static_admin',
            static_url_path='/static_url_admin',
            template_folder='template_admin'
        )


from admin.admin import admin
