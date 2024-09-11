from cache_service.lib.abcs.cache_abc import CacheABC
from redis import Redis
import os
import json

class RedisCacheService(CacheABC):
    instance = None
    def __init__(self):
        self.connection = Redis.from_url(os.getenv("REDIS_HOST", "redis://test"))
        
    def connect(self):
        self.connection.ping()
        return

    def disconnect(self):
        self.connection.close()
        return
    
    @staticmethod
    def get_instance() -> "RedisCacheService":
        if RedisCacheService.instance is None:
            RedisCacheService.instance = RedisCacheService()
            return RedisCacheService.instance
        return RedisCacheService.instance

    def get(self, key: str) -> dict:
        if not self.connection.exists(key): 
            return 

        data_str = self.connection.get(key)
        return json.loads(data_str)

    def set(self,key: str, data: dict) -> None:
        data_str = json.dumps(data)
        print(data_str, key)
        self.connection.set(key, data_str)
        return 

    def delete(self, key: str) -> None:
        if self.connection.exists(key):
            return self.connection.delete(key)
        return 