from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

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