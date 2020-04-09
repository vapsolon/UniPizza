from application import db
from application.models import Base
from application.models import OrderProduct

class Order(Base):

    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    products = db.relationship("OrderProduct", back_populates="order")

    def __init__(self, date, price):
        self.date = date
        self.price = price