from app.models.animals import Animals

def test_animals_models():
    animal = Animals(
    species="Lion",
    age="10",
    gender="Male",
    special_requirement="None"
)

    assert animal.species == "Lion"
    assert animal.age == "10"
    assert animal.gender == "Male"
    assert animal.special_requirement == "None"

    expected_dict = {
        "id": animal.id,
        "species": "Lion",
        "age": "10",
        "gender": "Male",
        "special_requirement": "None"
    }

    assert animal.as_dict() == expected_dict