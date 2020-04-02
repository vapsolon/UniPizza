from application import db
from application.models import Base
from application.models import product_ingredients

class Ingredient(Base):

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name