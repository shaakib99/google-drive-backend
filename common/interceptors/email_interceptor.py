from typing import Callable
from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC
from common.models.dependencies_model import CommonDependenciesModel
from user_service.service import UsersService
from typing import Any

class EmailInterceptor(InterceptorABC):
    def __init__(self, users_service = UsersService()):
        self.users_service = users_service
    
    async def intercept(self, next: Callable[..., Any], dependencies: CommonDependenciesModel, *args, **kwargs):
        request = dependencies.request
        url = request.url.path.lower()
        method = request.method.lower()
        body = await request.body()
        query_params = request.query_params

        result = await next(*args, dependencies = dependencies, **kwargs )

        if url == '/users/generate-reset-password-token' and method == 'post':
            # send email
            print('sending email...')

        return result

