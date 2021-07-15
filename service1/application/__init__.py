from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import holiday_plan
from application import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.142.113.223/holiday_plan"
app.config['SECRET_KEY'] = "root"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

