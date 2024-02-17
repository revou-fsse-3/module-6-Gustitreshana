import uuid
from sqlalchemy import UUID
from app.utils.database import db

class Animals(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    special_requirement = db.Column(db.String(200), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "species": self.species,
            "age": self.age,
            "gender": self.gender,
            "special_requirement": self.special_requirement
        }