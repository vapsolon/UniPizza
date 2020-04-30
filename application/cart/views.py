from application import app
from flask import render_template, request, redirect, url_for, session
from flask_login import current_user
from application.cart.forms import UserInfoForm
from application.product.models import Product

@app.route("/cart/", methods=["GET"])
def cart_index():
    if("cart" in session):
        items = []
        price = 0
        for item, amount in session["cart"].items():
            if(item != "total"):
                up = Product.query.get(item)
                up.amount = amount
                items.append(up)
                price += amount * up.price
        if not(current_user.is_authenticated):
            form = UserInfoForm(visible="yes")
        else:
            form = UserInfoForm(visible="no")
        return render_template("cart/cart.html", items=items, price=price, form=form)
    return redirect(url_for("menu_index"))
    
@app.route("/cart/<item_id>", methods=["GET"])
def cart_add(item_id):
    if not("cart" in session):
        session["cart"] = {item_id: 1, "total": 1}
    else:
        if not(item_id in session["cart"]):
            session["cart"][item_id] = 1
            session["cart"]["total"] += 1
            session.modified = True
        else:
            session["cart"][item_id] += 1
            session["cart"]["total"] += 1
            session.modified = True
    
    return redirect(url_for("menu_index"))
    
@app.route("/cart/<item_id>/remove", methods=["GET"])
def cart_remove(item_id):
    if("cart" in session):
        if(item_id in session["cart"]):
            if(session["cart"][item_id] > 1):
                session["cart"][item_id] -= 1
                session["cart"]["total"] -= 1
                session.modified = True
            else:
                del session["cart"][item_id]
                session["cart"]["total"] -= 1
                session.modified = True
        return redirect(url_for("cart_index"))
    return redirect(url_for("menu_index"))