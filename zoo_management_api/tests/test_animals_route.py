from app import app, db
import pytest
from app.models.animals import Animals

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_animals(client):
    with app.app_context():
        response = client.get('/animals/')
        assert response.status_code == 200

def test_get_animal(client):
    with app.app_context():
        animal = Animals(
            species="Lion",
            age="10",
            gender="Male",
            special_requirement="None"
        )
        db.session.add(animal)
        db.session.commit()

        response = client.get(f'/animals/{animal.id}')
        assert response.status_code == 200

def test_create_animal(client):
    with app.app_context():
        data = {
            "species": "Tiger",
            "age": "8",
            "gender": "Female",
            "special_requirement": "None"
        }
        response = client.post('/animals/', json=data)
        assert response.status_code == 201

def test_update_animal(client):
    with app.app_context():
        animal = Animals(
            species="Lion",
            age="10",
            gender="Male",
            special_requirement="None"
        )
        db.session.add(animal)
        db.session.commit()

        data = {
            "species": "Lion",
            "age": "12",
            "gender": "Male",
            "special_requirement": "None"
        }
        response = client.put(f'/animals/{animal.id}', json=data)
        assert response.status_code == 200

def test_delete_animal(client):
    with app.app_context():
        animal = Animals(
            species="Lion",
            age="10",
            gender="Male",
            special_requirement="None"
        )
        db.session.add(animal)
        db.session.commit()

        response = client.delete(f'/animals/{animal.id}')
        assert response.status_code == 200