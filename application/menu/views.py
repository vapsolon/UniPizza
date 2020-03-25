from application import app, db
from flask import render_template, request, redirect, url_for
from application.menu.models import Product
from application.menu.forms import ProductForm

@app.route("/", methods=["GET"])
def redirect_root():
    return render_template("menu/menu.html", menu = Product.query.all())

@app.route("/menu/", methods=["GET"])
def menu_index():
    return render_template("menu/menu.html", menu = Product.query.all())

@app.route("/menu/new")
def menu_form():
    return render_template("menu/new.html", form=ProductForm())

@app.route("/menu/", methods=["POST"])
def menu_add():
    form = ProductForm(request.form)
    
    if not form.validate():
        return render_template("menu/new.html", form=form)
    
    p = Product(
        form.name.data,
        form.ingredients.data,
        float(form.price.data)
    )

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("menu_index"))
    
    
@app.route("/menu/<item_id>/", methods=["GET"])
def menu_update_form(item_id):
    up = Product.query.get(item_id)
    return render_template("menu/update.html", item=up)

@app.route("/menu/<item_id>/", methods=["POST"])
def menu_update(item_id):
    up = Product.query.get(item_id)
    up.name = request.form.get("name")
    up.ingredients = request.form.get("ingredients")
    up.price = request.form.get("price")
    
    db.session.commit()
    return redirect(url_for("menu_index"))