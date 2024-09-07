from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app


def test_root_deve_retornar_ok_e_welcome():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Welcome to the main application'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        'login/register/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_get_users():
    client = TestClient(app)

    response = client.get('login/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user():
    client = TestClient(app)

    response = client.post(
        'login/users/1',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_delete_user():
    client = TestClient(app)

    response = client.delete('login/users/1')
    assert response.status_code == HTTPStatus.NO_CONTENT
