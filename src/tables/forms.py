from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TableForm(FlaskForm):
    name = StringField("Table name", [validators.Length(min=3,max=50)])
    columns = StringField("Table columns")
 
    class Meta:
        csrf = False