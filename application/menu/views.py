from application import app, db
from flask import render_template, redirect, url_for

from application.product.models import Product

@app.route("/", methods=["GET"])
def redirect_root():
    return redirect(url_for("menu_index"))

@app.route("/menu/", methods=["GET"])
def menu_index():
    return render_template("menu/menu.html", menu = Product.query.all())