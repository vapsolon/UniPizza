from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, validators
  
class UserInfoForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(), validators.length(min=2,max=140)])
    email = StringField("Email", [validators.InputRequired(), validators.length(min=2,max=140)])
    address = StringField("Address", [validators.InputRequired(), validators.length(min=2,max=140)])
    phone = StringField("Phone", [validators.InputRequired(), validators.length(min=2,max=140)])
    visible = HiddenField("Visible")
  
    class Meta:
        csrf = False