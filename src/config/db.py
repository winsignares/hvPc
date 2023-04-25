from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "cam123"

db = SQLAlchemy(app)

ma = Marshmallow(app)