from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.ingredient.models import Ingredient
from application.ingredient.forms import IngredientForm

@app.route("/ingredient/", methods=["GET"])
@login_required
def ingredient_index():
    return render_template("ingredient/list.html", ingredients = Ingredient.query.all())
    
@app.route("/ingredient/new", methods=["GET", "POST"])
@login_required
def ingredient_create():
    if(request.method == "GET"):
        if(current_user.admin == True):
            return render_template("ingredient/new.html", form=IngredientForm())
        else:
            return redirect(url_for("menu_index"))
    
    if(current_user.admin):
        form = IngredientForm(request.form)
        if not form.validate():
            return render_template("ingredient/new.html", form=form)

        i = Ingredient(
            form.name.data
        )
        
        db.session().add(i)
        db.session().commit()
        
        return redirect(url_for("ingredient_index"))
  
    return redirect(url_for("menu_index"))
    
@app.route("/ingredient/<item_id>/", methods=["GET", "POST"])
@login_required
def ingredient_update(item_id):
    if(request.method == "GET"):
        if(current_user.admin == True):
            up = Ingredient.query.get(item_id)
            return render_template("ingredient/update.html", form=IngredientForm(), item=up)
        else:
            return redirect(url_for("menu_index"))
            
    if(current_user.admin):
        up = Ingredient.query.get(item_id)
        
        form = IngredientForm(request.form)
        if not form.validate():
            return render_template("ingredient/update.html", form=form, item=up)
            
        up.name = form.name.data
        
        db.session.commit()
        return redirect(url_for("ingredient_index"))
    return redirect(url_for("menu_index"))
    
@app.route("/ingredient/<item_id>/delete", methods=["GET"])
@login_required
def ingredient_delete(item_id):
    if(current_user.admin):
        Ingredient.query.filter(Ingredient.id == item_id).delete()
        
        db.session.commit()
        return redirect(url_for("ingredient_index"))
    return redirect(url_for("menu_index"))