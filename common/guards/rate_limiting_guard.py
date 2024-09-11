from common.guards.lib.abcs.guard_abc import GuardABC
from common.models.dependencies_model import CommonDependenciesModel
from common.exceptions import TooManyRequestException
from common.models.rate_limiting_model import RateLimitingModel
from datetime import datetime


data = {}

class RateLimitingGuard(GuardABC):
    def __init__(self, max_token:int = 5, time_duration: int = 60):
        self.max_token = max_token
        self.time_duration = time_duration # seconds

    async def dispatch(self, dependencies: CommonDependenciesModel) -> tuple:
        request = dependencies.request
        client_host = request.client.host
        self.token_bucket_algorithm(client_host)
    
    def token_bucket_algorithm(self, key: str):
        if key not in data:
            data[key] = RateLimitingModel(available_token=self.max_token - 1, last_updated_at=datetime.now())
            return
        
        rate_limiting_info: RateLimitingModel = data[key]
        time_diff = (datetime.now() - rate_limiting_info.last_updated_at).seconds

        if time_diff < 60 and rate_limiting_info.available_token == 0:
            raise TooManyRequestException()
        
        if time_diff < 60 and rate_limiting_info.available_token > 0:
            rate_limiting_info.available_token = rate_limiting_info.available_token - 1

        if time_diff > 60:
            rate_limiting_info.available_token = self.max_token
    
        rate_limiting_info.last_updated_at = datetime.now()
        data[key] = rate_limiting_info

        
        

