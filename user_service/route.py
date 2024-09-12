from fastapi import APIRouter, Depends, File, UploadFile
from typing import Annotated
from database_service.models.query_param import QueryParamsModel
from user_service.service import UsersService
from user_service.models.request_models import CreateUserModel, UpdateUserModel
from user_service.models.response_models import UserResponseModel
from common.guards.jwt_auth_guard import JWTAuthGuard
from common.guards.rate_limiting_guard import RateLimitingGuard
from common.guards.use_guard import UseGuard
from common.models.dependencies_model import CommonDependenciesModel
from common.utils import inject_common_dependencies
from file_service.service import FileUploadService
from file_service.local_storage_provider import LocalStorageProvider
from common.interceptors.use_interceptor import UseInterceptor
from common.interceptors.cache_interceptor import CacheInterceptor

router = APIRouter(prefix='/users')

@router.get('', response_model=list[UserResponseModel], response_model_exclude_none=True)
async def getAll(
    query: Annotated[QueryParamsModel, Depends(QueryParamsModel)], 
    users_service: Annotated[UsersService, Depends(lambda: UsersService())]):
    return users_service.getAll(query)

@router.get('/{id}', response_model=UserResponseModel, response_model_exclude_none=True)
async def getOne(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.getOne(id)

@router.post('', response_model=UserResponseModel, response_model_exclude_none=True)
async def createOne(
    id: str, 
    data: CreateUserModel, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.createOne(data)

@router.patch('/{id}', response_model=UserResponseModel, response_model_exclude_none=True)
async def updateOne(
    id: str, 
    data: UpdateUserModel, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.updateOne(id, data)


@router.put('/update-profile-picture')
# @UseInterceptor(CacheInterceptor('test', 'ENDPOINT:'))
@UseGuard(RateLimitingGuard())
# @UseGuard(JWTAuthGuard())
async def updateProfilePicture(
    file: UploadFile,
    dependencies: Annotated[CommonDependenciesModel, Depends(inject_common_dependencies)],
    users_service: Annotated[UsersService, Depends(lambda: UsersService())],
    file_service: Annotated[FileUploadService, Depends(lambda: FileUploadService(LocalStorageProvider()))]
    ):
    return 'hello'

@router.delete('/{id}')
async def deleteOne(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.deleteOne(id)