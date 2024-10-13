from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    """
    Esquema para criação e atualização de usuários.

    Atributos:
        username (str): Nome de usuário.
        email (str): Endereço de e-mail do usuário.
        password (str): Senha do usuário.
    """

    username: str
    email: str
    password: str


class UserPublic(BaseModel):
    """
    Esquema para representação pública de usuários.

    Atributos:
        username (str): Nome de usuário.
        email (EmailStr): Endereço de e-mail do usuário (validado).
        id (int): Identificador único do usuário.
    """

    username: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    """
    Esquema para representação de usuários no banco de dados.

    Herda de UserSchema e adiciona:
        id (int): Identificador único do usuário.
    """

    id: int


class UserList(BaseModel):
    """
    Esquema para representação de uma lista de usuários.

    Atributos:
        users (list[UserPublic]): Lista de usuários no formato público.
    """

    users: list[UserPublic]
