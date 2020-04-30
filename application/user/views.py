from application import app
from flask import render_template
from flask_login import current_user, login_required
from application.auth.models import User

@app.route("/user", methods=["GET"])
@login_required
def user_index():
    if(current_user.admin == True):
        return render_template("user/users.html", users = User.query.all())
    else:
        return redirect(url_for("menu_index"))
    
@app.route("/user/<user_id>/", methods=["GET"])
@login_required
def specific_user(user_id):
    if(current_user.admin == True):
        return render_template("user/users.html", users = {User.query.get(user_id)})
    else:
        return redirect(url_for("menu_index"))