# dashboard/v1/routes.py

from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def read_dashboard():
    return {'message': 'Welcome to the Dashboard'}
