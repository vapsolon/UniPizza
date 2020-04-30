from application import db
from application.models import Base
from application.models import product_ingredients
from application.models import OrderProduct
from application.ingredient.models import Ingredient

from sqlalchemy.sql import text

class Product(Base):

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float, nullable=False)
    ingredients = db.relationship('Ingredient', secondary=product_ingredients,
        backref=db.backref("products"))
    orders = db.relationship("OrderProduct", back_populates="product")

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @staticmethod
    def sort_by_ingredient_count():
        statement = text("SELECT Product.id, Product.name, COUNT(Ingredient.id) FROM Product "
            " LEFT JOIN ProductIngredient ON ProductIngredient.product_id = Product.id "
            " LEFT JOIN Ingredient ON Ingredient.id = ProductIngredient.ingredient_id "
            " GROUP BY Product.id "
            " ORDER BY COUNT(Ingredient.id) DESC")
        response = db.engine.execute(statement)
        res = []
        for row in response:
            res.append({"id":row[0], "name":row[1], "count":row[2]})
        return res
    