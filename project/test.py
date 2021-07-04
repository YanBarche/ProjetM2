from flask import Flask, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect

 
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
SQLALCHEMY_ENGINE_OPTIONS = {
    "max_overflow": 15,
    "pool_pre_ping": True,
    "pool_recycle": 60 * 60,
    "pool_size": 30,
}
def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app)
    admin = Admin(name='My App')
    # Add views here
    app.config['SECRET_KEY'] = "kcavnjgnjvgkldm;c,kefjva"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:testyan@localhost/projetm2"
    db.init_app(app)
    
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import Users,MyModelView
    from admin_models import MyAdminIndexView
    admin.init_app(app,index_view=MyAdminIndexView())
    admin.add_view(MyModelView(Users,db.session))
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Users.query.get(int(user_id))
    return app

if __name__ == "__main__":
    app = create_app() 
    app.run(host="127.0.0.1",port="5000",debug=True)