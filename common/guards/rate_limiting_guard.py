from common.guards.lib.abcs.guard_abc import GuardABC
from common.models.dependencies_model import CommonDependenciesModel
from common.exceptions import TooManyRequestException
from common.models.rate_limiting_model import RateLimitingModel
from cache_service.service import CacheService
from datetime import datetime



class RateLimitingGuard(GuardABC):
    def __init__(self, max_token:int = 5, time_duration: int = 60, cache_service = CacheService()):
        self.max_token = max_token
        self.time_duration = time_duration # seconds
        self.cache_service = cache_service

    async def dispatch(self, dependencies: CommonDependenciesModel) -> tuple:
        request = dependencies.request
        client_host = request.client.host
        self.token_bucket_algorithm(f"RATE_LIMIT:{client_host}")
    
    def token_bucket_algorithm(self, key: str):
        data = self.cache_service.get(key)
        if data is None:
            rate_limiter = RateLimitingModel(available_token=self.max_token - 1, last_updated_at=datetime.now().isoformat())
            self.cache_service.set(key, rate_limiter.model_dump())
            return
        rate_limiting_info: RateLimitingModel = RateLimitingModel.model_validate(data)
        rate_limiter_last_updated_at = datetime.fromisoformat(rate_limiting_info.last_updated_at)

        time_diff = (datetime.now() - rate_limiter_last_updated_at).seconds

        if time_diff <= self.time_duration and rate_limiting_info.available_token == 0:
            raise TooManyRequestException()
        
        if time_diff < self.time_duration and rate_limiting_info.available_token > 0:
            rate_limiting_info.available_token = rate_limiting_info.available_token - 1

        if time_diff > self.time_duration:
            rate_limiting_info.available_token = self.max_token - 1
    
        rate_limiting_info.last_updated_at = datetime.now().isoformat()
        self.cache_service.set(key, rate_limiting_info.model_dump())

        
        

