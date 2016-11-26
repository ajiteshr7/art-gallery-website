from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, ValidationError, PasswordField
from wtforms import validators, ValidationError
from models import db, User

class SignupForm(Form):
    firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    phone_number = TextField("Phone number")
    gender = TextField("gender")
    address = TextField("address")
    city = TextField("city")
    country = TextField("country")
    submit = SubmitField("Create account")

def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

def validate(self):
    if not Form.validate(self):
        return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True

class SigninForm(Form):
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False

class FeedbackForm(Form):
    name = TextField("Name", [validators.Required("Please enter your first name.")],description="Name" )
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")],description="Email")
    subject = TextField("Name", [validators.Required("Please enter your first name.")],description="Subject" )
    comment = TextField("Name", [validators.Required("Please enter your first name.")],description="Comment" )
    submit = SubmitField("Send Message")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

class SubmitArt(Form):
    name = TextField("Name", [validators.Required("Please enter paintings title.")],description="Painting's title" )
    location = TextField("Location", [validators.Required("Please enter file location.")],description="Paintings's location" )
    artist_id = TextField("Artist_id", [validators.Required("Please enter artist_id.")],description="Artist_id" )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
