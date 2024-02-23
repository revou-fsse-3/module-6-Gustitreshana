from app.models.employees import Employees

def test_employees_models():
    employee = Employees(
        name="Gusti Herman",
        email="gusti.herman@gmail.com",
        phone_number="08123456789",
        role="Manager",
        schedule="Everyday"
    )
    
    assert employee.name == "Gusti Herman"
    assert employee.email == "gusti.herman@gmail.com"
    assert employee.phone_number == "08123456789"
    assert employee.role == "Manager"
    assert employee.schedule == "Everyday"
    
    expected_dict = {
        "id": employee.id,
        "name": "Gusti Herman",
        "email": "gusti.herman@gmail.com",
        "phone_number": "08123456789",
        "role": "Manager",
        "schedule": "Everyday"
    }
    
    assert employee.as_dict() == expected_dict
        