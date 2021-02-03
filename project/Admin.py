from flask_admin import Admin
from test import create_app

app = create_app()

admin = Admin(app, "Blog Admin")

if __name__ == "__main__":
    app = create_app() 
    app.run(host="127.0.0.1",port="5000",debug=True)