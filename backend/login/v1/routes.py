# login/v1/routes.py

from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from login.v1.schemas import UserDB, UserList, UserPublic, UserSchema

router = APIRouter()

database = []


@router.get('/')
def read_login():
    """
    Rota de boas-vindas para o sistema de login.

    Retorna:
        dict: Uma mensagem de boas-vindas.
    """
    return {'message': 'Welcome to the Login'}


@router.post(
    '/register', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    """
    Cria um novo usuário no sistema.

    Args:
        user (UserSchema): Os dados do usuário a ser criado.

    Retorna:
        UserPublic: Os dados públicos do usuário criado.

    Raises:
        HTTPException: Se houver um erro ao criar o usuário.
    """
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@router.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    """
    Retorna a lista de todos os usuários cadastrados.

    Retorna:
        UserList: Uma lista contendo todos os usuários.
    """
    return {'users': database}


@router.post(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    """
    Atualiza os dados de um usuário existente.

    Args:
        user_id (int): O ID do usuário a ser atualizado.
        user (UserSchema): Os novos dados do usuário.

    Retorna:
        UserPublic: Os dados públicos do usuário atualizado.

    Raises:
        HTTPException: Se o usuário não for encontrado.
    """
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@router.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    """
    Remove um usuário do sistema.

    Args:
        user_id (int): O ID do usuário a ser removido.

    Raises:
        HTTPException: Se o usuário não for encontrado.
    """
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    database.pop(user_id - 1)
