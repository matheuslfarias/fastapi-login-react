# login/v1/routes.py

from http import HTTPStatus

from fastapi import APIRouter

from login.v1.schemas import UserDB, UserPublic, UserSchema

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
