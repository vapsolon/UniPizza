from application import db
from application.models import Base

from sqlalchemy.sql import text

class Ingredient(Base):

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def sort_by_most_products():
        statement = text("SELECT Ingredient.id, Ingredient.name, COUNT(Product.id) FROM Ingredient "
            " LEFT JOIN ProductIngredient ON ProductIngredient.ingredient_id = Ingredient.id "
            " LEFT JOIN Product ON Product.id = ProductIngredient.product_id "
            " GROUP BY Ingredient.id "
            " ORDER BY COUNT(Product.id) DESC")
        response = db.engine.execute(statement)
        res = []
        for row in response:
            res.append({"id":row[0], "name":row[1], "count":row[2]})
        return res