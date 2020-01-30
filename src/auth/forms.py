from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.Email()])
    password = PasswordField("Password", [validators.length(min=6)])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    email = StringField("Email", [validators.Email()])
    password = PasswordField("Password", [validators.length(min=6)])
  
    class Meta:
        csrf = False