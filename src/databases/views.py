from src import app, db
from flask import redirect, render_template, request, url_for
from src.databases.models import Database

@app.route("/databases", methods=["GET"])
def databases_index():
    return render_template("list.html", databases = Database.query.all())

@app.route("/databases/new/")
def databases_form():
    return render_template("new.html")

@app.route("/databases/<database_id>/", methods=["POST"])
def database_change_name(database_id):

    t = Database.query.get(database_id)
    t.name = "new name"
    db.session().commit()
  
    return redirect(url_for("databases_index"))

@app.route("/databases/", methods=["POST"])
def databases_create():
    item = Database(request.form.get("name"))
  
    db.session().add(item)
    db.session().commit()

    return "hello world!"