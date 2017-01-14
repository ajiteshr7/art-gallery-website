from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash,check_password_hash

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), nullable = False ,unique = True)
    pwdhash = db.Column(db.String(54), nullable = False)
    phone_number = db.Column(db.String(15), nullable = False)
    gender = db.Column(db.String(30), nullable = False)
    address = db.Column(db.String(50), nullable = False)
    city = db.Column(db.String(30), nullable = False)
    country = db.Column(db.String(30), nullable = False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def __init__ (self, firstname="", lastname="", email="", password="", phone_number="", gender="", address="", city="", country=""):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
        self.phone_number = phone_number
        self.gender = gender.upper()
        self.address = address
        self.city = city.title()
        self.country = country.title()

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash,password)

class Artist(db.Model):
    __tablename__='artist'
    artist_id = db.Column(db.Integer, primary_key = True)
    artist_bio = db.Column(db.String(100), nullable = False)
    artist_name = db.Column(db.String(100),nullable = False)
    artist_city = db.Column(db.String(30), nullable = False )
    artist_country = db.Column(db.String(30), nullable = False )
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    def __init__ (self, artist_name="", artist_bio="", artist_city="",artist_country=""):
        self.artist_name = artist_name.title()
        self.artist_bio = artist_bio
        self.artist_city = artist_city.title()
        self.artist_country = artist_country.title()

    def __repr__(self):
        return '<Artist %r>' % self.artist_name

class Paintings(db.Model):
    __tablename__='paintings'
    painting_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    painting_photo = db.Column(db.String(100), nullable = False)
    artist_id = db.Column(db.Integer,db.ForeignKey(Artist.artist_id), nullable = False )
    painting_bio = db.Column(db.String(100), default = "Beautiful art piece")
    painter = db.relationship('Artist', foreign_keys='Paintings.artist_id')
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def __init__(self, name="", painting_photo="", artist_id=1):
        self.name = name.title()
        self.painting_photo = painting_photo
        self.artist_id = artist_id

    def __repr__(self):
        return '<Painting %r>' % self.name


class Feedback(db.Model):
    __tablename__='feedback'
    feed_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    subject = db.Column(db.String(50) )
    comment = db.Column(db.String(200))
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def __init__ (self, name="", email="", subject="", comment=""):
        self.name = name.title()
        self.email = email.lower()
        self.subject = subject.title()
        self.comment = comment


class AdminUser(db.Model):
    __tablename__ = 'admin_user'
    admin_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    pwd = db.Column(db.String(54), nullable = False)

    def __init__ (self, name="", email="", password=""):
        self.name = name.title()
        self.email = email.lower()
        self.pwd = password

    def check_password(self, password):
        return (self.pwd == password)
