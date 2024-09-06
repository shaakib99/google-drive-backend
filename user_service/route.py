from fastapi import APIRouter, Depends
from typing import Annotated
from database_service.models.query_param import QueryParamsModel
from user_service.service import UsersService
from user_service.models.request_models import CreateUserModel, UpdateUserModel
from user_service.models.response_models import UserResponseModel
from common.interceptors.use_interceptor import UseInterceptor
from common.interceptors.response_interceptor import ResponseInterceptor
from common.guards.jwt_auth_guard import JWTAuthGuard
from common.guards.use_guard import UseGuard
from common.models.dependencies import CommonDependencies

router = APIRouter(prefix='/users')

@router.get('', response_model=list[UserResponseModel], response_model_exclude_none=True)
async def getAll(
    query: Annotated[QueryParamsModel, Depends(QueryParamsModel)], 
    users_service: Annotated[UsersService, Depends(UsersService)]):
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


@router.put('/{id}')
@UseGuard(JWTAuthGuard())
@UseInterceptor(ResponseInterceptor())
async def updateFile(
    id: str, 
    CommonDependencies: Annotated[CommonDependencies, Depends(CommonDependencies)]):
    print(CommonDependencies.user)
    return 'hello'

@router.delete('/{id}')
async def deleteOne(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.deleteOne(id)