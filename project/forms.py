import wtforms

class AddUserForm(wtforms.Form):
    username = wtforms.StringField("Username")
    password = wtforms.StringField("Password")