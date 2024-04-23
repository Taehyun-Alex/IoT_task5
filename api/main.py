import casbin
from fastapi import FastAPI
from fastapi_authz import CasbinMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

import basic_auth

api = FastAPI()

enforcer = casbin.Enforcer(
    'rbac_model.conf',
    'rbac_policy.csv',
)
backend = basic_auth.BasicAuth()

api.add_middleware(CasbinMiddleware, enforcer=enforcer)
api.add_middleware(AuthenticationMiddleware, backend=backend)

@api.get('/')
async def index():
    return 'Hello, world.'
