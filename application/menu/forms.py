from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ProductForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    ingredients = StringField("Ingredients", [validators.InputRequired()])
    price = StringField("Price", [validators.InputRequired()])
 
    class Meta:
        csrf = False