from application import app
from flask import render_template
from application.auth.models import User

@app.route("/user", methods=["GET"])
def user_index():
    return render_template("user/users.html", users = User.query.all())
    
@app.route("/user/<user_id>/", methods=["GET"])
def specific_user(user_id):
    return render_template("user/users.html", users = {User.query.get(user_id)})