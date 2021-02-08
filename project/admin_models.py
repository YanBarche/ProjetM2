from utils import is_admin
from flask_admin import AdminIndexView
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return is_admin()