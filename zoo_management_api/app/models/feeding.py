import uuid
from app.utils.database import db
from sqlalchemy import UUID

class Feeding(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    animal_id = db.Column(db.String(50), nullable=False)
    enclosure_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    food_type = db.Column(db.String(50), nullable=False)
    feeding_time = db.Column(db.String(50), nullable=False)

def as_dict(self):
    return {
        "id": self.id,
        "food_type": self.food_type,
        "feeding_time": self.feeding_time
    }
