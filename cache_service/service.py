from cache_service.lib.abcs.cache_abc import CacheABC
from cache_service.redis_cache_service import RedisCacheService

class CacheService:
    def __init__(self, service = RedisCacheService):
        self.service: CacheABC = service.get_instance()
    
    def connect(self):
        return self.service.connect()
    
    def disconnect(self):
        return self.service.disconnect()
    
    def get(self, key: str) -> dict:
        return self.service.get(key)

    def set(self, key: str, data: dict) -> None:
        return self.service.set(key, data)

    def delete(self, key: str) -> None:
        return self.service.delete(key)