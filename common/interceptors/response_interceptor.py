from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC
from typing import Callable
from common.models.dependencies import CommonDependencies

class ResponseInterceptor(InterceptorABC):
    def __init__(self):
        pass

    async def intercept(self, 
        next: Callable, 
        dependencies:CommonDependencies, 
        *args, 
        **kwargs):
        res = await next(*args, **kwargs)
        return res