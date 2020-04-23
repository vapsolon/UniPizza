from application import db
from application.models import Base

class Order(Base):

    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    products = db.relationship("OrderProduct", back_populates="order")
    user_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    user = db.relationship("User", back_populates="orders")

    def __init__(self, date, price):
        self.date = date
        self.price = price