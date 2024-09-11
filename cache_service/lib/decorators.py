from cache_service.service import CacheService
from functools import wraps
from common.utils import generate_cache_key

def cache(key: str, prefix: str = 'CACHE:'):
    def wrapper(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            cache_service = CacheService()

            new_key = generate_cache_key(key, prefix, f"{args}{kwargs}")
            data = cache_service.get(new_key) 
            if data is not None: 
                return data
            
            result = await func(*args, **kwargs)
            cache_service.set(new_key, result)
            return result
        return inner
    return wrapper

