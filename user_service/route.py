from fastapi import APIRouter, Depends, UploadFile
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
from common.interceptors.use_interceptor import UseInterceptor
from common.interceptors.cache_interceptor import CacheInterceptor
from common.interceptors.validate_cache_interceptor import ValidateCacheInterceptor

router = APIRouter(prefix='/users')

@router.get('', response_model=list[UserResponseModel], response_model_exclude_none=True)
async def getAll(
    query: Annotated[QueryParamsModel, Depends(QueryParamsModel)], 
    users_service: Annotated[UsersService, Depends(lambda: UsersService())],
    dependencies: Annotated[CommonDependenciesModel, Depends(inject_common_dependencies)]):
    return users_service.getAll(query)

@router.get('/{id}', response_model=UserResponseModel, response_model_exclude_none=True)
@UseInterceptor(CacheInterceptor('users.one'))
async def getOne(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.getOne(id)

@router.post('', response_model=UserResponseModel, response_model_exclude_none=True)
async def createOne(
    data: CreateUserModel, 
    users_service: Annotated[UsersService, Depends(lambda: UsersService())]):
    return users_service.createOne(data)

@router.patch('', response_model=UserResponseModel, response_model_exclude_none=True)
@UseGuard(JWTAuthGuard())
@UseGuard(RateLimitingGuard())
async def updateOne(
    id: str, 
    data: UpdateUserModel, 
    users_service: Annotated[UsersService, Depends(UsersService)],
    dependencies: Annotated[CommonDependenciesModel, Depends(inject_common_dependencies)]):
    return users_service.updateOne(id, data)


@router.put('/update-profile-picture')
@UseGuard(JWTAuthGuard())
@UseGuard(RateLimitingGuard())
@UseInterceptor(ValidateCacheInterceptor('users.one'))
async def updateProfilePicture(
    file: UploadFile,
    users_service: Annotated[UsersService, Depends(lambda: UsersService())],
    dependencies: Annotated[CommonDependenciesModel, Depends(inject_common_dependencies)]
    ):
    return await users_service.update_profile_picture(file, dependencies.user)

@router.delete('')
@UseGuard(JWTAuthGuard())
async def deleteOne(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)],
    dependencies: Annotated[CommonDependenciesModel, Depends(inject_common_dependencies)]):
    return users_service.deleteOne(id)