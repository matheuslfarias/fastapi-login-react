from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app


def test_root_deve_retornar_ok_e_welcome():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Welcome to the main application'}
