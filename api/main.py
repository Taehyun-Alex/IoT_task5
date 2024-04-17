import casbin
from fastapi import FastAPI

api = FastAPI()

enforcer = casbin.Enforcer(
    'rbac_model.conf',
    'rbac_policy.csv',
)

@api.get('/')
async def index():
    return 'Hello, world.'
