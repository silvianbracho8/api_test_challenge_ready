import uuid

class PersonAPI:
    def __init__(self):
        # Simulamos una "base de datos" en memoria
        self.persons = {}

    def create_person(self, data):
        # Simula una creación exitosa
        person_id = str(uuid.uuid4())
        self.persons[person_id] = data
        data_with_id = data.copy()
        data_with_id["personId"] = person_id
        return MockResponse(201, data_with_id)

    def get_person(self, person_id):
        # Devuelve persona si existe, error si no
        if person_id in self.persons:
            result = self.persons[person_id].copy()
            result["personId"] = person_id
            return MockResponse(200, result)
        else:
            return MockResponse(404, {"error": "Person not found"})

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data

    def json(self):
        return self._json