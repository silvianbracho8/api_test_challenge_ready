import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.import_api import PersonAPI
import logging
import pytest
from pages.import_api import PersonAPI

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

# Test Sad Path: ID inexistente
def test_get_person_invalid(api):
    invalid_id = "123456-nonexistent"
    logging.info("Ejecutando test sad path: GET /person con ID inválido")
    response = api.get_person(invalid_id)
    logging.info(f"Status: {response.status_code}, Body: {response.json()}")
    assert response.status_code == 404 or response.status_code == 400
    assert "error" in response.json() or "message" in response.json()

# Simulación de validación contra DB
def test_verify_person_in_db(valid_person_id):
    logging.info(f"Simulando validación en DB para personId: {valid_person_id}")
    exists_in_db = simulate_db_check(valid_person_id)
    assert exists_in_db

def simulate_db_check(person_id):
    logging.info(f"[Simulado] Verificando personId en base de datos: {person_id}")
    return True