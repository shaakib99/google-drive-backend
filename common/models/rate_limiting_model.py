from pydantic import BaseModel
from datetime import datetime

class RateLimitingModel(BaseModel):
    available_token: int
    last_updated_at: datetime