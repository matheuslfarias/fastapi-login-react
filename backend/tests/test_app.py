from http import HTTPStatus

from login.v1.schemas import UserPublic


def test_root_deve_retornar_ok_e_welcome(client):
    """
    Testa se a rota raiz retorna o status OK e a mensagem de
    boas-vindas correta.
    """

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Welcome to the main application'}


def test_create_user(client):
    """
    Testa a criação de um novo usuário através da rota de registro.
    """

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


def test_get_users(client):
    """
    Testa a obtenção da lista de usuários cadastrados.
    """

    response = client.get('login/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('login/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client):
    """
    Testa a atualização dos dados de um usuário existente.
    """

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


def test_not_found_put_user(client):
    """
    Testa a tentativa de atualização de um usuário inexistente.
    """

    response = client.post(
        'login/users/10',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    """
    Testa a remoção de um usuário existente.
    """

    response = client.delete('login/users/1')
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_not_found_delete_user(client):
    """
    Testa a tentativa de remoção de um usuário inexistente.
    """

    response = client.delete('login/users/10')
    assert response.status_code == HTTPStatus.NOT_FOUND
