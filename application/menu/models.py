from application import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    ingredients = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price