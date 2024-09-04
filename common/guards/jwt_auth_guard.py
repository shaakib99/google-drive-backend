from common.lib.abcs.guard_abc import GuardABC
from user_service.schemas.user_schema import UserSchema
from user_service.service import UsersService
from fastapi import Request, Response
from common.exceptions import UnauthorizeException
from jwt import decode
import os

class JWTAuthGuard(GuardABC):
    def __init__(self, users_service = UsersService()):
        self.users_service = UsersService

    def invoke_guard(self, req: Request , res: Response):
        token = req.headers.get('X-DRIVE-TOKEN')

        if not token:
            raise UnauthorizeException()
        
        return self.validate_token(token)
    
    def validate_token(self, token: str) -> UserSchema:
        user_dict = decode(token, os.getenv('JWT_SECRET'), algorithms='HS256')
        if 'id' not in user_dict:
            raise UnauthorizeException()

        user = self.users_service.getOne(user_dict['id'])
        if not user: 
            raise UnauthorizeException()
        
        return user
