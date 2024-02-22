from flask import Blueprint, request, jsonify
from app.models.feeding import Feeding
from app.utils.database import db

feeding_schedule_blueprint = Blueprint('feeding_endpoint', __name__)

@feeding_schedule_blueprint.route("/", methods=["GET"])
def get_feeding_schedule():
    try:
        feeding_schedule = Feeding.query.all()
        return jsonify([feeding.as_dict() for feeding in feeding_schedule]), 200
    except Exception as e:
        return str(e), 404
    
@feeding_schedule_blueprint.route("/<string:id>", methods=["GET"])
def get_feeding(id):
    try:
        feeding = Feeding.query.get(id)
        return jsonify(feeding.as_dict()), 200
    except Exception as e:
        return str(e), 404
    
@feeding_schedule_blueprint.route("/", methods=["POST"])
def create_feeding():
    try:
        data = request.json
        feeding = Feeding()
        feeding.animal_id = data['animal_id']
        feeding.food_type = data['food_type']
        feeding.feeding_time = data['feeding_time']
        db.session.add(feeding)
        db.session.commit()
        return 'Feeding schedule created successfully', 201
    except Exception as e:
        return str(e), 404
    
@feeding_schedule_blueprint.route('/<string:id>', methods=['PUT'])
def update_feeding(id):
    try:
        feeding = Feeding.query.get(id)
        data = request.json
        feeding.animal_id = data['animal_id']
        feeding.food_type = data['food_type']
        feeding.feeding_time = data['feeding_time']
        db.session.commit()
        return 'Feeding schedule updated successfully', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 404
    
@feeding_schedule_blueprint.route('/<string:id>', methods=['DELETE'])
def delete_feeding(id):
    try:
        feeding = Feeding.query.get(id)
        db.session.delete(feeding)
        db.session.commit()
        return 'Feeding schedule deleted successfully', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 404