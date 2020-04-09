from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.product.models import Product
from application.product.forms import ProductForm
from application.ingredient.models import Ingredient

@app.route("/product/new")
def product_form():
    if(current_user.get_id() != None and current_user.admin):
        form = ProductForm()
        form.ingredients.choices = [(i.id, i.name) for i in Ingredient.query.all()]
        form.ingredients.data = [i.id for i in Ingredient.query.all()]
        return render_template("product/new.html", form=form)
    else:
        return redirect(url_for("menu_index"))

@app.route("/product/", methods=["POST"])
def product_add():
    if(current_user.get_id() != None and current_user.admin):
        form = ProductForm(request.form)
        form.ingredients.choices = [(i.id, i.name) for i in Ingredient.query.all()]
        
        if not form.validate():
            return render_template("product/new.html", form=form)
        
        p = Product(form.name.data, form.price.data)
        for ingredient in form.ingredients.data:
            i = Ingredient.query.get(ingredient)
            p.ingredients.append(i)

        db.session().add(p)
        db.session().commit()
      
    return redirect(url_for("menu_index"))
        
@app.route("/product/<item_id>/", methods=["GET"])
def product_update_form(item_id):
    if(current_user.get_id() != None and current_user.admin):
        up = Product.query.get(item_id)
        form = ProductForm()
        form.ingredients.choices = [(i.id, i.name) for i in Ingredient.query.all()]
        form.ingredients.data = [i.id for i in Ingredient.query.all()]
        return render_template("product/update.html", item=up, form=form)
    else:
        return redirect(url_for("menu_index"))

@app.route("/product/<item_id>/", methods=["POST"])
def product_update(item_id):
    if(current_user.get_id() != None and current_user.admin):
        up = Product.query.get(item_id)
        
        form = ProductForm(request.form)
        form.ingredients.choices = [(i.id, i.name) for i in Ingredient.query.all()]
        if not form.validate():
            return render_template("product/update.html", item=up, form=form)
            
        up.name = form.name.data
        up.price = float(form.price.data)
        up.ingredients = []
        for ingredient in form.ingredients.data:
            i = Ingredient.query.get(ingredient)
            up.ingredients.append(i)
        
        db.session.commit()
    return redirect(url_for("menu_index"))
    
@app.route("/product/<item_id>/delete", methods=["GET"])
def product_delete(item_id):
    if(current_user.get_id() != None and current_user.admin):
        p = Product.query.get(item_id)
        
        db.session.delete(p)
        db.session.commit()
    return redirect(url_for("menu_index"))
    
@app.route("/product/stats/", methods=["GET"])
def product_stats():
    return render_template("product/stats.html", stats = Product.sort_by_ingredient_count())