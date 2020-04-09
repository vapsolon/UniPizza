from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, validators
  
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.InputRequired(), validators.length(min=2,max=140)])
    password = PasswordField("Password", [validators.InputRequired(), validators.length(min=2,max=140)])
  
    class Meta:
        csrf = False
        
class CreateForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(), validators.length(min=2,max=140)])
    email = StringField("Email", [validators.InputRequired(), validators.length(min=2,max=140)])
    password = PasswordField("Password", [validators.InputRequired(), validators.length(min=2,max=140)])
    address = StringField("Address", [validators.InputRequired(), validators.length(min=2,max=140)])
    phone = StringField("Phone", [validators.InputRequired(), validators.length(min=2,max=140)])
    admin = BooleanField("Admin")
  
    class Meta:
        csrf = False