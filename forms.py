from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField


class ContactForm(FlaskForm):

    name = StringField("Full Name")

    email = StringField("Email Address")

    message = TextAreaField("Message")

    submit = SubmitField("Send Message")