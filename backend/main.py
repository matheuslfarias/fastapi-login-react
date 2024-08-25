# main.py

from fastapi import FastAPI

from dashboard.v1.routes import router as dashboard_router
from login.v1.routes import router as login_router

app = FastAPI()

# Inclui os routers nas rotas principais
app.include_router(dashboard_router, prefix='/dashboard')
app.include_router(login_router, prefix='/login')


@app.get('/')
def read_root():
    return {'message': 'Welcome to the main application'}
