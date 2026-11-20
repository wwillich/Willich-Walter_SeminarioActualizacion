import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from main import app  # noqa: E402

VALIDO = {"age": 50, "bmi": 27.1, "bp": 93}
ORIGEN_OK = "http://localhost:5500"


@pytest.fixture
def client():
    with TestClient(app) as c:  # el `with` dispara el lifespan (carga del modelo)
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"estado": "ok"}


def test_predecir_valido(client):
    r = client.post("/predecir", json=VALIDO)
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body["prediccion"], float)
    assert 50 < body["prediccion"] < 350


@pytest.mark.parametrize(
    "payload",
    [
        {"age": 50, "bmi": 27.1},                       # falta bp
        {**VALIDO, "bmi": "abc"},                       # tipo incorrecto
        {**VALIDO, "age": "50"},                        # string numérico no se acepta (strict)
        {**VALIDO, "extra": 1},                         # campo de más
        {**VALIDO, "bmi": 500},                         # fuera de rango
        {},                                             # vacío
    ],
)
def test_predecir_invalido_422(client, payload):
    assert client.post("/predecir", json=payload).status_code == 422


def test_predecir_error_interno_500(client):
    original = app.state.modelo

    class Roto:
        feature_names_in_ = ["age", "bmi", "bp"]

        def predict(self, X):
            raise RuntimeError("boom")

    app.state.modelo = Roto()
    try:
        r = client.post("/predecir", json=VALIDO)
    finally:
        app.state.modelo = original
    assert r.status_code == 500
    assert r.json() == {"detail": "Error interno al predecir"}


def test_cors_origen_permitido(client):
    r = client.options(
        "/predecir",
        headers={
            "Origin": ORIGEN_OK,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        },
    )
    assert r.status_code == 200
    assert r.headers["access-control-allow-origin"] == ORIGEN_OK


def test_cors_origen_no_permitido(client):
    r = client.options(
        "/predecir",
        headers={
            "Origin": "https://malicioso.example",
            "Access-Control-Request-Method": "POST",
        },
    )
    assert "access-control-allow-origin" not in r.headers
