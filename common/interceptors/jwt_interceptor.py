from fastapi import Response
from typing import Callable, Any
from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC
from common.models.dependencies_model import CommonDependenciesModel
from user_service.models.user_model import UserModel
import jwt
import os

class JWTInterceptor(InterceptorABC):
    def __init__(self):
        pass

    async def intercept(self, next: Callable[..., Any], dependencies: CommonDependenciesModel, *args, **kwargs):
        response = dependencies.response

        kwargs['dependencies'] = dependencies
        res = await next(*args, **kwargs)

        user = UserModel.model_validate(res)
        jwt_token = jwt.encode({'id': user.id}, os.getenv('JWT_SECRET'), algorithm='HS256')

        response.headers['X-DRIVE-KEY'] = jwt_token

        return res

