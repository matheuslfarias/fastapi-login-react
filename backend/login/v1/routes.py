# login/v1/routes.py

from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from login.v1.schemas import UserDB, UserList, UserPublic, UserSchema

router = APIRouter()

database = []


@router.get('/')
def read_login():
    return {'message': 'Welcome to the Login'}


@router.post(
    '/register', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@router.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@router.post(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@router.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    database.pop(user_id - 1)
