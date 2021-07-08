from application import db

class holiday_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city= db.Column(db.String(100), nullable=False, unique=True)
    activity= db.Column(db.String(100), nullable=False), unique=True
    price =  db.Column(db.Integer, nullable=False)