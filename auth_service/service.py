from database_service.service import DatabaseService
from user_service.schemas.user_schema import UserSchema
from auth_service.models.auth_models import LoginModel, GenerateResetPasswordTokenModel, ResetPasswordModel
from user_service.models.user_model import UserModel
from common.exceptions import NotFoundException, BadRequestException
from common.utils import hash_password
from database_service.models.query_param import QueryParamsModel
from datetime import datetime, timedelta

class AuthService:
    def __init__(self, model: DatabaseService[UserSchema] = DatabaseService(UserSchema)):
        self.user_model = model
    
    async def login(self, loginModel: LoginModel):
        encrypted_password = hash_password(loginModel.password)
        query  = QueryParamsModel()
        query.limit = 1
        query.filter_by = "email='%s' and password='%s'" % (loginModel.email, encrypted_password)

        users = self.user_model.getAll(query)

        if len(users) == 0:
            raise NotFoundException('Email and password not found')
        return users[0]
        
    async def reset_password(self, data:ResetPasswordModel):
        query = QueryParamsModel()
        query.limit = 1
        query.filter_by = "password_reset_token=%s" % (data.token)
        users = self.user_model.getAll(query)

        if len(users) == 0:
            raise NotFoundException('token not found')
        
        user = users[0]

        current_datetime = datetime.now()
        if (current_datetime - user.password_reset_token_generated_at) > timedelta(minutes=30):
            raise BadRequestException('token expired')

        user.password = data.new_password
        user.updated_at = datetime.now()
        user.password_reset_token = None
        user = self.user_model.updateOne(user.id, UserModel.model_validate(user))
        return user


    async def generate_password_reset_token(self, data: GenerateResetPasswordTokenModel):
        query = QueryParamsModel()
        query.limit = 1
        query.filter_by = "email='%s'" % (data.email)
        users = self.user_model.getAll(query)
        
        if len(users) == 0:
            raise NotFoundException("Email not found")
        
        user = users[0]

        user.password_reset_token = ''
        user.password_reset_token_generated_at = datetime.now()
        user = self.user_model.updateOne(user.id, UserModel.model_validate(user))

        return user
