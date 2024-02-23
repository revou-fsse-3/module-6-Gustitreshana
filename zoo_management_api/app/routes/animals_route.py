from flask import Blueprint, request
from app.models.animals import Animals
from app.utils.database import db

animals_blueprint = Blueprint('animals_endpoint', __name__)

@animals_blueprint.route("/", methods=["GET"])
def get_animals():
    try:
        animals = Animals.query.all()
        return [animal.as_dict() for animal in animals], 200
    except Exception as e:
        return str(e), 404

@animals_blueprint.route("/<string:id>", methods=["GET"])
def get_animal(id):
    try:
        animal = db.session.get(Animals, id)
        return animal.as_dict(), 200
    except Exception as e:
        return str(e), 404

@animals_blueprint.route("/", methods=["POST"])
def create_animal():
    try:
        data = request.json
        animal = Animals()
        animal.species = data['species']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.special_requirement = data['special_requirement']
        db.session.add(animal)
        db.session.commit()
        return 'Animal created successfully', 201
    except Exception as e:
        return str(e), 404

@animals_blueprint.route('/<string:id>', methods=['PUT'])
def update_animal(id):
    try:
        animal = db.session.get(Animals, id)
        data = request.json
        animal.species = data['species']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.special_requirement = data.get('special_requirement', '')
        db.session.commit()
        return 'Animal updated successfully', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 404

@animals_blueprint.route('/<string:id>', methods=['DELETE'])
def delete_animal(id):
    try:
        animal = db.session.get(Animals, id)
        db.session.delete(animal)
        db.session.commit()
        return 'Animal deleted successfully', 200
    except Exception as e:
        return str(e), 404


