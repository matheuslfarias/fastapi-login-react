from dataclasses import asdict

from sqlalchemy import select

from login.v1.models import User


def test_create_user(session, mock_db_time):
    """
    Testa a criação de um novo usuário no banco de dados.

    Este teste verifica se um novo usuário pode ser criado, adicionado
    à sessão,persistido no banco de dados e posteriormente recuperado
    com sucesso.

    Args:
        session (Session): Fixture que fornece uma sessão de banco de
        dados para o teste.

    Passos do teste:
    1. Cria um novo usuário com dados de exemplo.
    2. Adiciona o usuário à sessão e realiza o commit.
    3. Consulta o banco de dados para recuperar o usuário criado.
    4. Verifica se o usuário recuperado tem o nome de usuário correto.
    """
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
    }
