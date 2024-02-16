from app.utils.database import db

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    schedule = db.Column(db.String(200))

