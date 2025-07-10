# API Test Challenge – Automatización con Pytest

Este proyecto fue desarrollado como respuesta a un challenge técnico para automatizar pruebas sobre una API REST. Se implementaron pruebas de tipo **happy path** y **sad path**, siguiendo buenas prácticas de estructura y reutilización de código con el patrón **POM (Page Object Model)**, adaptado para API Testing.

---

## Requisitos Técnicos

- Python 3.10 o superior (usado: 3.13)
- Pytest (`pip install -r requirements.txt`)
- Estructura modular basada en POM
- Parametrización dinámica de `personId`
- Manejo básico de errores y validaciones

---

## 📁 Estructura del Proyecto

api_test_challenge_ready/
├── api_pytest_tests/
│ └── api_test_enhanced.py # Archivo principal con casos de prueba
├── pages/
│ ├── init.py # Define módulo pages
│ └── import_api.py # Lógica POM simulando la API
├── tests/
│ ├── test_import.py # Otros tests iniciales
│ └── test_import_2.py
├── conftest.py # Fixtures compartidos
├── requirements.txt # Dependencias
└── README.md # Este archivo


---

## Cómo ejecutar los tests

# API Test Challenge – Automatización con Pytest

Este proyecto fue desarrollado como respuesta a un challenge técnico para automatizar pruebas sobre una API REST. Se implementaron pruebas de tipo **happy path** y **sad path**, siguiendo buenas prácticas de estructura y reutilización de código con el patrón **POM (Page Object Model)**, adaptado para API Testing.

---

## 🚀 Requisitos Técnicos

- Python 3.10 o superior (usado: 3.13)
- Pytest (`pip install -r requirements.txt`)
- Estructura modular basada en POM
- Parametrización dinámica de `personId`
- Manejo básico de errores y validaciones

---

## 📁 Estructura del Proyecto

```
api_test_challenge_ready/
├── api_pytest_tests/
│   └── api_test_enhanced.py       # Archivo principal con casos de prueba
├── pages/
│   ├── __init__.py                # Define módulo pages
│   └── import_api.py             # Lógica POM simulando la API
├── tests/
│   ├── test_import.py            # Otros tests iniciales
│   └── test_import_2.py
├── conftest.py                   # Fixtures compartidos
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

---

## 🧪 Cómo ejecutar los tests

Desde la raíz del proyecto, ejecutar:

```bash
py -m pytest -s api_pytest_tests/api_test_enhanced.py
```

O para correr todo el conjunto de pruebas:

```bash
py -m pytest -s
```

---

## ✅ Casos implementados

- `test_create_person_happy`: Crea una persona válida y verifica la respuesta
- `test_get_person_valid`: Consulta una persona existente
- `test_get_person_invalid`: Verifica comportamiento cuando `personId` no existe

---

## 🛠️ Extras implementados

- Uso de fixtures (`api`, `valid_person_id`, `auth_headers`)
- Logs informativos con `logging`
- Separación clara del modelo API y las pruebas
- Preparado para extender a tests reales con `requests`

---

## 🧩 Futuras mejoras sugeridas

- Conexión real con una API externa (remplazar mock por `requests`)
- Validación contra base de datos (opcional)
- Generación de reportes HTML (`pytest-html`)
- CI/CD con GitHub Actions o GitLab CI

---

## ✍️ Autora

Silvia Bracho  
