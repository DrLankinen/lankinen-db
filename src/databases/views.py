from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from src import app, db
from src.databases.models import Database
from src.databases.forms import DatabaseForm

@app.route("/databases/", methods=["GET"])
@login_required
def databases_index():
    return render_template("databases/list.html", databases = Database.query.all())

@app.route("/databases/new/")
@login_required
def databases_form():
    return render_template("databases/new.html", form = DatabaseForm())

@app.route("/databases/<database_id>/", methods=["GET", "POST"])
@login_required
def database_change_name(database_id):
    if request.method == "GET":
        return render_template("databases/details.html", database = Database.query.get(database_id))

    t = Database.query.get(database_id)
    t.name = "new name"
    db.session().commit()
  
    return redirect(url_for("databases_index"))

@app.route("/databases/", methods=["POST"])
@login_required
def databases_create():
    form = DatabaseForm(request.form)
  
    if not form.validate():
        return render_template("databases/new.html", form = form)

    item = Database(form.name.data)
    item.account_id = current_user.id
    
    db.session().add(item)
    db.session().commit()

    return redirect(url_for("databases_index"))