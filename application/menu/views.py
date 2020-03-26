from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.menu.models import Product
from application.menu.forms import ProductForm

@app.route("/", methods=["GET"])
def redirect_root():
    return redirect(url_for("menu_index"))

@app.route("/menu/", methods=["GET"])
def menu_index():
    return render_template("menu/menu.html", menu = Product.query.all())

@app.route("/menu/new")
def menu_form():
    if(current_user.get_id() != None and current_user.admin):
        return render_template("menu/new.html", form=ProductForm())
    else:
        return redirect(url_for("menu_index"))

@app.route("/menu/", methods=["POST"])
def menu_add():
    if(current_user.get_id() != None and current_user.admin):
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
    if(current_user.get_id() != None and current_user.admin):
        up = Product.query.get(item_id)
        return render_template("menu/update.html", item=up, form=ProductForm())
    else:
        return redirect(url_for("menu_index"))

@app.route("/menu/<item_id>/", methods=["POST"])
def menu_update(item_id):
    if(current_user.get_id() != None and current_user.admin):
        up = Product.query.get(item_id)
        
        form = ProductForm(request.form)
        if not form.validate():
            return render_template("menu/update.html", form=form)
            
        up.name = form.name.data
        up.ingredients = form.ingredients.data
        up.price = float(form.price.data)
        
        db.session.commit()
    return redirect(url_for("menu_index"))
    
@app.route("/menu/<item_id>/delete", methods=["GET"])
def menu_delete(item_id):
    if(current_user.get_id() != None and current_user.admin):
        Product.query.filter(Product.id == item_id).delete()
        
        db.session.commit()
    return redirect(url_for("menu_index"))