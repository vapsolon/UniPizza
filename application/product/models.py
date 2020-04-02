from application import db
from application.models import Base
from application.models import product_ingredients
from application.ingredient.models import Ingredient

class Product(Base):

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float, nullable=False)
    ingredients = db.relationship('Ingredient', secondary=product_ingredients,
        backref=db.backref("products"))

    def __init__(self, name, price):
        self.name = name
        self.price = price