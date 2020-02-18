from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DatabaseForm(FlaskForm):
    name = StringField("Database name", [validators.Length(min=3,max=50)])
 
    class Meta:
        csrf = False

class RenameDatabaseForm(FlaskForm):
    name = StringField("Rename Database", [validators.Length(min=3,max=50)])
 
    class Meta:
        csrf = False