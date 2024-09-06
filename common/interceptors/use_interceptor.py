from functools import wraps
from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC

class UseInterceptor:
    def __init__(self, interceptor: InterceptorABC):
        self.interceptor = interceptor

    def __call__(self, func: callable):
        @wraps(func)
        async def wrappper(*args, **kwargs):
            dependencies = kwargs.get('CommonDependencies')
            return await self.interceptor.intercept(func, dependencies, *args, **kwargs)
        return wrappper