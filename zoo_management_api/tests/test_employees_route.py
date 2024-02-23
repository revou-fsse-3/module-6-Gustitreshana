from app import app, db
import pytest
from app.models.employees import Employees

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_get_employees(client):
    with app.app_context():
        response = client.get('/employees/')
        assert response.status_code == 200
        
def test_get_employee(client):
    with app.app_context():
        employee = Employees(
            name="Gusti Herman",
            email="gusti.herman@gmail.com",
            phone_number="08123456789",
            role="Manager",
            schedule="Everyday"
        )
        db.session.add(employee)
        db.session.commit()
        
        response = client.get(f'/employees/{employee.id}')
        assert response.status_code == 200
        
def test_create_employee(client):
    with app.app_context():
        data = {
            "name": "Gusti Herman",
            "email": "gusti.herman@gmail.com",
            "phone_number": "08123456789",
            "role": "Manager",
            "schedule": "Everyday"
        }
        response = client.post('/employees/', json=data)
        assert response.status_code == 201
        
def test_update_employee(client):
    with app.app_context():
        employee = Employees(
            name="Gusti Herman",
            email="gusti.herman@gmail.com",
            phone_number="08123456789",
            role="Manager",
            schedule="Everyday"
        )
        db.session.add(employee)
        db.session.commit()
        
        data = {
            "name": "Gusti Herman",
            "email": "gusti.herman@gmail.com",
            "phone_number": "08123456789",
            "role": "Manager",
            "schedule": "Everyday"
        }
        response = client.put(f'/employees/{employee.id}', json=data)
        assert response.status_code == 200

def test_delete_employee(client):
    with app.app_context():
        employee = Employees(
            name="Gusti Herman",
            email="gusti.herman@gmail.com",
            phone_number="08123456789",
            role="Manager",
            schedule="Everyday"
        )
        db.session.add(employee)
        db.session.commit()
        
        response = client.delete(f'/employees/{employee.id}')
        assert response.status_code == 200