from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo
)
from wtforms import SubmitField


class ContactForm(FlaskForm):

        name = StringField("Full Name")

        email = StringField("Email Address")

        message = TextAreaField("Message")

        submit = SubmitField("Send Message")

class LoginForm(FlaskForm):

    username = StringField("Username", validators=[
            DataRequired(),
            Length(min=3, max=30)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    remember_me = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Login"
    )
    

class RegistrationForm(FlaskForm):
    username = StringField(
    "Username",
    validators=[
    DataRequired(),
    Length(min=3, max=30)
        ]
    )

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField("Register")