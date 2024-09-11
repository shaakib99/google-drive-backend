from database_service.models.query_param import QueryParamsModel
from database_service.service import DatabaseService
from user_service.schemas.user_schema import UserSchema
from common.exceptions import NotFoundException
from user_service.models.request_models import CreateUserModel, UpdateUserModel

class UsersService:
    def __init__(self, user_model = DatabaseService(UserSchema)):
        self.user_model = user_model
    
    def getOne(self, id: str):
        user = self.user_model.getOne(id)
        if not user:
            raise NotFoundException(f'{id} not found')
        return user
    
    def getAll(self, query: QueryParamsModel):
        return self.user_model.getAll(query)
    
    def createOne(self, data: CreateUserModel):
        return self.user_model.createOne(data)
    
    def updateOne(self, id: int, data: UpdateUserModel):
        return self.user_model.updateOne(id, data)
    
    def deleteOne(self, id: int):
        return self.user_model.deleteOne(id)