from application import app, db, bcrypt
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application.auth.models import User
from application.auth.forms import LoginForm, CreateForm

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if(request.method == "GET"):
        return render_template("auth/login.html", form=LoginForm())
        
    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("auth/login.html", form=form)

    user = User.query.filter_by(email=form.email.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "No such email or password")
    
    if(bcrypt.check_password_hash(user.password, form.password.data)):
        login_user(user)
        return redirect(url_for("menu_index"))
    else:
        return render_template("auth/login.html", form = form,
                               error = "No such email or password")
    
@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("menu_index"))
    
@app.route("/auth/new", methods=["GET", "POST"])
def account_create():
    if(request.method == "GET"):
        if(current_user.get_id() == None):
            return render_template("auth/new.html", form=CreateForm(), admin = False)
        elif(current_user.admin == True):
            return render_template("auth/new.html", form=CreateForm(), admin = True)
        else:
            return redirect(url_for("menu_index"))
    
    form = CreateForm(request.form)
    admin = form.admin.data
    if not form.validate():
        return render_template("auth/new.html", form=form, admin=admin)
        
    hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

    u = User(
        form.name.data,
        form.email.data,
        hash,
        form.address.data,
        form.phone.data,
        admin
    )
    
    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("menu_index"))