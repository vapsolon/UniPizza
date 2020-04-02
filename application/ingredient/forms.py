from flask_wtf import FlaskForm
from wtforms import StringField, validators

class IngredientForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
 
    class Meta:
        csrf = False