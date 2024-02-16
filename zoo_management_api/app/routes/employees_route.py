from flask import Blueprint, jsonify, request
from models.employees import Employees
from app.utils.database import db

employees_blueprint = Blueprint('employees_endpoint', __name__)

@employees_blueprint.route('/', methods=['GET'])
def get_employees():
    employees = Employees.query.all()
    return jsonify([employee.serialize() for employee in employees])

@employees_blueprint.route('/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employees.query.get_or_404(id)
    return jsonify(employee.serialize())

@employees_blueprint.route('/', methods=['POST'])
def create_employee():
    data = request.json
    if not all(key in data for key in ['name', 'email', 'phone_number', 'role']):
        return jsonify({'error': 'Missing required fields'}), 400

    employee = Employees(name=data['name'], email=data['email'], phone_number=data['phone_number'], role=data['role'], schedule=data.get('schedule', ''))
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee created successfully'}), 201

@employees_blueprint.route('/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employees.query.get_or_404(id)
    data = request.json
    if not all(key in data for key in ['name', 'email', 'phone_number', 'role']):
        return jsonify({'error': 'Missing required fields'}), 400

    employee.name = data['name']
    employee.email = data['email']
    employee.phone_number = data['phone_number']
    employee.role = data['role']
    employee.schedule = data.get('schedule', '')
    db.session.commit()
    return jsonify({'message': 'Employee updated successfully'})

@employees_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employees.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully'})