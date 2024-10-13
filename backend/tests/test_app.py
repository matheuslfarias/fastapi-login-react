from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app


def test_root_deve_retornar_ok_e_welcome():
    """
    Testa se a rota raiz retorna o status OK e a mensagem de
    boas-vindas correta.
    """
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Welcome to the main application'}


def test_create_user():
    """
    Testa a criação de um novo usuário através da rota de registro.
    """
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
    """
    Testa a obtenção da lista de usuários cadastrados.
    """
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
    """
    Testa a atualização dos dados de um usuário existente.
    """
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


def test_not_found_put_user():
    """
    Testa a tentativa de atualização de um usuário inexistente.
    """
    client = TestClient(app)

    response = client.post(
        'login/users/10',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user():
    """
    Testa a remoção de um usuário existente.
    """
    client = TestClient(app)

    response = client.delete('login/users/1')
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_not_found_delete_user():
    """
    Testa a tentativa de remoção de um usuário inexistente.
    """
    client = TestClient(app)

    response = client.delete('login/users/10')
    assert response.status_code == HTTPStatus.NOT_FOUND
