from pydantic import BaseModel
from fastapi import Request, Response
from user_service.models.user_model import UserModel
from typing import Optional

class CommonDependencies(BaseModel):
    request: Request
    user: Optional[UserModel] = None

    class Config:
        arbitrary_types_allowed=True

