from os import environ
from flask import Flask

app = Flask(__name__)

app.secret_key = 'mnbvcxz92+iobugvy554576*()%~`5rsaxfi8716jhajh$^*'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'mysql://root:1234@127.0.0.1:3306/art_gallery')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['BASIC_AUTH_USERNAME'] = 'admin'
# app.config['BASIC_AUTH_PASSWORD'] = 'admin'
# app.config['BASIC_AUTH_FORCE'] = True

from models import db
db.init_app(app)

from flask_migrate import Migrate

migrate = Migrate(app,db)

import art_web.views
