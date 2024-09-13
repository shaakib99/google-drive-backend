from pydantic import BaseModel
from fastapi import Request, Response
from user_service.models.user_model import UserModel
from typing import Optional

class CommonDependenciesModel(BaseModel):
    request: Request
    response: Response
    user: Optional[UserModel] = None

    class Config:
        arbitrary_types_allowed=True

