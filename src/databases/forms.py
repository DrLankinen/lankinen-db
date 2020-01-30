from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DatabaseForm(FlaskForm):
    name = StringField("Database name", [validators.Length(min=3)])
 
    class Meta:
        csrf = False