from typing import Callable, Any
from common.interceptors.lib.abcs.interceptor_abc import InterceptorABC
from cache_service.service import CacheService
from common.models.dependencies_model import CommonDependenciesModel
from common.utils import generate_cache_key

class ValidateCacheInterceptor(InterceptorABC):
    def __init__(self, key: str, prefix: str = 'CACHE:', cache_service = CacheService()):
        self.cache_service = cache_service
        self.key = key
        self.prefix = prefix
    
    def intercept(self, next: Callable[..., Any], dependencies: CommonDependenciesModel, *args, **kwargs):
        request = dependencies.request
        query_params = request.query_params
        headers = request.headers


        kwargs['dependencies'] = dependencies
        result = next(*args, **kwargs)

        cache_key = generate_cache_key(self.key, self.prefix, f"{query_params}")

        if self.cache_service.get(cache_key) is None:
            return result

        self.cache_service.set(cache_key, result)
        return result