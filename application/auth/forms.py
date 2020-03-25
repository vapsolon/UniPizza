from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
  
    class Meta:
        csrf = False
        
class CreateForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    email = StringField("Email", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    address = StringField("Address", [validators.InputRequired()])
    phone = StringField("Phone", [validators.InputRequired()])
  
    class Meta:
        csrf = False