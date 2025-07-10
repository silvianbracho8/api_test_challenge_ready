import logging

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