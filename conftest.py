import pytest
from pages.import_api import PersonAPI

@pytest.fixture
def api():
    return PersonAPI()

@pytest.fixture
def auth_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer xxx"
    }

@pytest.fixture
def valid_person_id(api):
    response = api.create_person({"name": "Silvia", "age": 25})
    return response.json()["personId"]
