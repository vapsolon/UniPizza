from application import app, db
from flask import render_template, request, redirect, url_for
from application.menu.models import Product

@app.route("/menu/", methods=["GET"])
def menu_index():
    return render_template("menu/menu.html", menu = Product.query.all())

@app.route("/menu/new")
def menu_form():
    return render_template("menu/new.html")

@app.route("/menu/", methods=["POST"])
def menu_add():
    p = Product(
        request.form.get("name"),
        request.form.get("ingredients"),
        float(request.form.get("price"))
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