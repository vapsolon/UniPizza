import datetime
from application import app, db
from flask import render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from application.order.models import Order
from application.auth.models import User
from application.models import OrderProduct
from application.cart.forms import UserInfoForm

from application.product.models import Product

@app.route("/order", methods=["GET"])
@login_required
def order_index():
    if(current_user.admin == True):
        return render_template("order/orders.html", orders = Order.query.all())
    else:
        return redirect(url_for("menu_index"))
      
@app.route("/order/<order_id>/", methods=["GET"])
@login_required
def specific_order(order_id):
    if(current_user.admin == True):
        return render_template("order/orders.html", orders = {Order.query.get(order_id)})
    else:
        return redirect(url_for("menu_index"))
    
@app.route("/order/user/<user_id>/", methods=["GET"])
@login_required
def orders_for_user(user_id):
    if(current_user.id == int(user_id)):
        u = User.query.get(user_id)
        orders = []
        for order in u.orders:
            orders.append(Order.query.get(order.id))
        return render_template("order/orders.html", orders = orders)
    else:
        return redirect(url_for("menu_index"))

@app.route("/order/confirmed", methods=["GET"])
def order_confirmed():
    return render_template("order/confirmed.html")

@app.route("/order/send/<price>", methods=["GET", "POST"])
def order_send(price):
    if("cart" in session):
        form = UserInfoForm(request.form)
        if(form.visible.data == "yes"):
            if not form.validate():
                return redirect(url_for("cart_index"))
            
        o = Order(datetime.datetime.now(), price)
        if not(current_user.is_authenticated):
            o.user = None
        else:
            o.user = current_user
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