from flask import Blueprint, request
from app.models.employees import Employees
from app.utils.database import db

employees_blueprint = Blueprint('employees_endpoint', __name__)

@employees_blueprint.route('/', methods=['GET'])
def get_employees():
    try:
        employees = Employees.query.all()
        return [employee.as_dict() for employee in employees]
    except Exception as e:
        return str(e), 404 

@employees_blueprint.route('/<string:id>', methods=['GET'])
def get_employee(id):
    try:
        employee = Employees.query.get(id)
        return employee.as_dict(), 200
    except Exception as e:
        return str(e), 404


@employees_blueprint.route('/', methods=['POST'])
def create_employee():
    try:
        data = request.json
        employee = Employees()
        employee.name = data['name']
        employee.email = data['email']
        employee.phone_number = data['phone_number']
        employee.role = data['role']
        employee.schedule = data.get('schedule')
        db.session.add(employee)
        db.session.commit()
        return 'Employee created successfully', 201
    except Exception as e:
        return str(e), 404

@employees_blueprint.route('/<string:id>', methods=['PUT'])
def update_employee(id):
    try:
        employee = Employees.query.get(id)
        data = request.json
        employee.name = data['name']
        employee.email = data['email']
        employee.phone_number = data['phone_number']
        employee.role = data['role']
        employee.schedule = data.get('schedule', '')
        db.session.commit()
        return 'Employee updated successfully', 200
    except Exception as e:
        return str(e), 404

@employees_blueprint.route('/<string:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        employee = Employees.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return 'Employee deleted successfully', 200
    except Exception as e:
        return str(e), 404