from pydantic import BaseModel
from fastapi import Request, Response
from user_service.models.user_model import UserModel

class CommonDependencies(BaseModel):
    request: Request
    response: Response
    user: UserModel | None = None

    class Config:
        arbitrary_types_allowed=True