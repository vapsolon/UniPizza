from application import db

product_ingredients = db.Table("ProductIngredient",
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
    db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredient.id"))
)

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())