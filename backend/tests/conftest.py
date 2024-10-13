from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from login.v1.models import table_registry
from main import app


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(model, 'before_insert', fake_time_hook)
    yield time

    event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time


@pytest.fixture
def client():
    """
    Fixture que fornece um cliente de teste para a aplicação FastAPI.

    Retorna:
        TestClient: Um cliente de teste para fazer requisições à aplicação.
    """
    return TestClient(app)


@pytest.fixture
def session():
    """
    Fixture que cria uma sessão de banco de dados em memória para testes.

    Esta fixture configura um banco de dados SQLite em memória, cria as tabelas
    necessárias, fornece uma sessão para os testes e, em seguida, limpa o banco
    de dados após o uso.

    Yields:
        Session: Uma sessão SQLAlchemy para interagir com o banco de dados de
        teste.
    """
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
