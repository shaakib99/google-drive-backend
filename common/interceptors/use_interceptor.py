from functools import wraps
from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC
from fastapi import Request, Depends
from common.models.dependencies_model import CommonDependenciesModel

class UseInterceptor:
    def __init__(self, interceptor: InterceptorABC):
        self.interceptor = interceptor

    def __call__(self, func: callable):
        @wraps(func)
        async def wrappper(*args,  **kwargs):
            dependencies: CommonDependenciesModel = kwargs.get('dependencies')
            del kwargs['dependencies']
            return await self.interceptor.intercept(func, dependencies, *args, **kwargs)
        return wrappper