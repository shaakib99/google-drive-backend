from database_service.models.query_param import QueryParamsModel
from database_service.service import DatabaseService
from user_service.schemas.user_schema import UserSchema
from user_service.models.user_model import UserModel
from common.exceptions import NotFoundException
from user_service.models.request_models import CreateUserModel, UpdateUserModel
from file_service.service import FileUploadService
from cache_service.service import CacheService
from common.utils import hash_password
from fastapi import UploadFile
from datetime import datetime

class UsersService:
    def __init__(self, user_model = DatabaseService(UserSchema), file_upload_service = FileUploadService(), cache_service = CacheService()):
        self.user_model = user_model
        self.file_upload_service = file_upload_service
        self.cache_service = cache_service
    
    def getOne(self, id: str):
        user = self.user_model.getOne(id)
        if not user:
            raise NotFoundException(f'{id} not found')
        return user
    
    def getAll(self, query: QueryParamsModel):
        return self.user_model.getAll(query)
    
    def createOne(self, data: CreateUserModel):
        data.password = hash_password(data.password)
        return self.user_model.createOne(data)
    
    def updateOne(self, id: int, data: UpdateUserModel):
        user = self.getOne(id)
        user_model = UserModel.model_validate(user)

        for key, value in data.model_dump().items():
            setattr(user_model, key, value)

        user_model.updated_at = datetime.now()
        
        return self.user_model.updateOne(id, user_model)
    
    def deleteOne(self, id: int):
        self.getOne(id)
        return self.user_model.deleteOne(id)
    
    async def update_profile_picture(self, file: UploadFile, user: UserModel):
        file = await self.file_upload_service.upload(file, user)

        user.profile_picture_id = file.id

        return self.updateOne(user.id, user)
