from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from src import app, db
from src.auth.models import User
from src.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Incorrect email or password")
    
    login_user(user)

    return redirect(url_for("index"))

@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/new.html", form = RegisterForm())

    form = RegisterForm(request.form)

    item = User(form.email.data,form.password.data)
    db.session().add(item)
    db.session().commit()

    return redirect(url_for("databases_index"))