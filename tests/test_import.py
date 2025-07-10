import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
import pytest
from api.person_api import PersonAPI

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fixture para instancia de API
@pytest.fixture(scope="module")
def api():
    return PersonAPI()

# Fixture para crear un personId válido
@pytest.fixture
def valid_person_id(api):
    logging.info("Creando persona de prueba para obtener personId válido")
    response = api.create_person({"name": "QA Test", "age": 30})
    assert response.status_code == 201
    person_id = response.json().get("personId")
    logging.info(f"personId creado: {person_id}")
    return person_id

# Test Happy Path
def test_get_person_valid(api, valid_person_id):
    logging.info("Ejecutando test happy path: GET /person con ID válido")
    response = api.get_person(valid_person_id)
    logging.info(f"Status: {response.status_code}, Body: {response.json()}")
    assert response.status_code == 200
    assert "name" in response.json()
    assert response.json().get("personId") == valid_person_id

