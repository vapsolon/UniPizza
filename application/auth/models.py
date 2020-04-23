from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    orders = db.relationship("Order", back_populates="user")

    def __init__(self, name, email, password, address, phone, admin):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True