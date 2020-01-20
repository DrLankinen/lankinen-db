from src import app, db
from flask import render_template, request
from src.dbs.models import Database

@app.route("/db/new/")
def db_form():
    return render_template("db/new.html")

@app.route("/db/", methods=["POST"])
def db_create():
    item = Database(request.form.get("name"))
  
    db.session().add(t)
    db.session().commit()

    return "hello world!"