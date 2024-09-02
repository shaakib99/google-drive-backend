from fastapi import APIRouter, Depends
from typing import Annotated
from database_service.models.query_param import QueryParamsModel
from user_service.service import UsersService
from user_service.models.request_models import CreateUserModel, UpdateUserModel
from user_service.models.response_models import UserResponseModel

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

@router.post('')
async def createOne(
    id: str, 
    data: CreateUserModel, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.createOne(data)

@router.patch('/{id}')
async def updateOne(
    id: str, 
    data: UpdateUserModel, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.updateOne(id, data)

@router.put('/{id}')
async def updateFile(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    pass

@router.delete('/{id}')
async def deleteOne(
    id: str, 
    users_service: Annotated[UsersService, Depends(UsersService)]):
    return users_service.deleteOne(id)