# login/v1/routes.py

from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def read_login():
    return {'message': 'Welcome to the Login'}
