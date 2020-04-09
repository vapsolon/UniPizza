from flask_wtf import FlaskForm
from wtforms import StringField, validators

class IngredientForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(), validators.length(min=2,max=140)])
 
    class Meta:
        csrf = False