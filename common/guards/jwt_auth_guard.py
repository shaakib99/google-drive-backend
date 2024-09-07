from common.guards.lib.abcs.guard_abc import GuardABC
from user_service.schemas.user_schema import UserSchema
# from user_service.service import UsersService
from common.exceptions import UnauthorizeException
from common.models.dependencies import CommonDependencies
from user_service.models.user_model import UserModel
from fastapi import Depends
from jwt import decode
import os

class JWTAuthGuard(GuardABC):
    def __init__(self, users_service = None):
        self.users_service = users_service

    async def dispatch(self, dependecies: CommonDependencies):
        req = dependecies.request
        # token = req.headers.get('X-DRIVE-KEY')

        # if not token:
        #     raise UnauthorizeException()
        
        # user = await self.validate_token(token)
        # dependecies.user = UserModel.model_validate(user)
    
    def validate_token(self, token: str) -> UserSchema:
        user_dict = decode(token, os.getenv('JWT_SECRET'), algorithms='HS256')
        if 'id' not in user_dict:
            raise UnauthorizeException()

        user = self.users_service.getOne(user_dict['id'])
        if not user: 
            raise UnauthorizeException()
        
        return user