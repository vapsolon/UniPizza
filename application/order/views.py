import datetime
from application import app, db
from flask import render_template, request, redirect, url_for, session
from application.order.models import Order
from application.models import OrderProduct

from application.product.models import Product

@app.route("/order", methods=["GET"])
def order_index():
    return render_template("order/orders.html", orders = Order.query.all())

@app.route("/order/confirmed", methods=["GET"])
def order_confirmed():
    return render_template("order/confirmed.html")

@app.route("/order/send/<price>", methods=["GET"])
def order_send(price):
    if("cart" in session):
        o = Order(datetime.datetime.now(), price)
        for item, amount in session["cart"].items():
            if(item != "total"):
                op = OrderProduct(amount = amount)
                op.product = Product.query.get(item)
                o.products.append(op)

        db.session().add(o)
        db.session().commit()
        session.pop("cart")
        return redirect(url_for("order_confirmed"))
    return redirect(url_for("menu_index"))