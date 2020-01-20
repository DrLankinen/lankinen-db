from src import app, db
from flask import render_template, request
from src.databases.models import Database

@app.route("/databases", methods=["GET"])
def databases_index():
    return render_template("databases/list.html", tasks = Database.query.all())

@app.route("/databases/new/")
def databases_form():
    return render_template("databases/new.html")

@app.route("/databases/", methods=["POST"])
def databases_create():
    item = Database(request.form.get("name"))
  
    db.session().add(item)
    db.session().commit()

    return "hello world!"