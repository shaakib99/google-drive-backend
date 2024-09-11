from typing import Callable, Any
from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC
from common.models.dependencies_model import CommonDependenciesModel
from cache_service.service import CacheService
from common.utils import generate_cache_key

class CacheInterceptor(InterceptorABC):
    def __init__(self, key: str, prefix: str = 'CACHE:', cache_service = CacheService()):
        self.key = key
        self.prefix = prefix
        self.cache_service = cache_service
    
    async def intercept(self, next: Callable[..., Any], dependencies: CommonDependenciesModel, *args, **kwargs):
        request = dependencies.request
        query_params = request.query_params
        headers = request.headers

        key = generate_cache_key(self.key, self.prefix, f"{query_params}")
        data = self.cache_service.get(key)

        
        if data is not None:
            return data
        
        kwargs['dependencies'] = dependencies
        result = await next(*args, **kwargs)

        self.cache_service.set(key, result)

        return result