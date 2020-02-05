from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from src import app, db
from src.tables.models import Table
from src.tables.forms import TableForm

@app.route("/tables/", methods=["GET"])
@login_required
def tables_index():
    return render_template("tables/list.html", tables = Table.query.all())

@app.route("/tables/new", methods=["POST"])
@login_required
def tables_create():
    form = TableForm(request.form)
  
    if not form.validate():
        return render_template("tables/new.html", form = form)

    item = Table(form.name.data, form.columns.data)
    
    db.session().add(item)
    db.session().commit()

    return redirect(url_for("tables_index"))