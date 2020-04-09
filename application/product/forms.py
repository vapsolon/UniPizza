from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, widgets, SelectMultipleField

class IngredientsSelection(SelectMultipleField):
    widget = widgets.ListWidget()
    option_widget = widgets.CheckboxInput()
    
    def pre_validate(self, form):
        '''Disable pre-validation because it's a pain right now'''

class ProductForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(), validators.length(min=2,max=12)])
    price = DecimalField("Price", [validators.InputRequired()])
    ingredients = IngredientsSelection("Ingredients", [validators.InputRequired()])
 
    class Meta:
        csrf = False