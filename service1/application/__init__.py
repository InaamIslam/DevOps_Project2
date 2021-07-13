from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://
app.config['SECRET_KEY'] = 'random'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes