from application import db

product_ingredients = db.Table("productingredient",
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
    db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredient.id"))
)

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
        
class OrderProduct(db.Model):
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
        
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    amount = db.Column(db.Integer)
    product = db.relationship("Product", back_populates="orders")
    order = db.relationship("Order", back_populates="products")