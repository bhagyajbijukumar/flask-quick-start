from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class SignUpForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(),Length(min=4, max=16)])
    email = StringField("email", validators=[Length(min=6,max=36)])
    password = PasswordField("password", validators=[Length(min=6, max=18)])
    confirm_password = PasswordField("confim_password", validators=[EqualTo("password")])
    submit = SubmitField()