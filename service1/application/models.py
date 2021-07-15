from application import db

class holiday_plan(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    city= db.Column(db.String(100), nullable=False,)
    activity= db.Column(db.String(100), nullable=False) 
    price =  db.Column(db.String(100), nullable=False)

