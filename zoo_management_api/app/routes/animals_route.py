from flask import Blueprint, jsonify, request
from models.animals import Animals
from app.utils.database import db

animals_blueprint = Blueprint('animals_endpoint', __name__)

@animals_blueprint.route("/", methods=["GET"])
def get_animals():
    try:
        animals = Animals.query.all()
        return jsonify([animal.serialized() for animal in animals])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@animals_blueprint.route("/<int:id>", methods=["GET"])
def get_animal(id):
    try:
        animal = Animals.query.get_or_404(id)
        return jsonify(animal.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@animals_blueprint.route("/", methods=["POST"])
def create_animal():
    try:
        data = request.json
        animal = Animals(species=data['species'], age=data['age'], gender=data['gender'], special_requirement=data.get('special_requirement', ''))
        db.session.add(animal)
        db.session.commit()
        return jsonify({'message': 'Animal created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@animals_blueprint.route('/<int:id>', methods=['PUT'])
def update_animal(id):
    try:
        animal = Animals.query.get_or_404(id)
        data = request.json
        animal.species = data['species']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.special_requirement = data.get('special_requirement', '')
        db.session.commit()
        return jsonify({'message': 'Animal updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 404

@animals_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_animal(id):
    try:
        animal = Animals.query.get_or_404(id)
        db.session.delete(animal)
        db.session.commit()
        return jsonify({'message': 'Animal deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 404


