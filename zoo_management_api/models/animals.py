from app.utils.database import db

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    special_requirement = db.Column(db.String(200))