from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.Email(), validators.length(max=100)])
    password = PasswordField("Password", [validators.length(min=6,max=100)])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    email = StringField("Email", [validators.Email(), validators.length(max=100)])
    password = PasswordField("Password", [validators.length(min=6), validators.length(max=100)])
  
    class Meta:
        csrf = False