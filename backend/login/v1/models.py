from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    """
    Representa um usuário no sistema.

    Atributos:
        id (int): Identificador único do usuário, gerado automaticamente.
        username (str): Nome de usuário único.
        password (str): Senha do usuário.
        email (str): Endereço de e-mail único do usuário.
        created_at (datetime): Data e hora de criação do usuário,
        definida automaticamente.
    """

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
