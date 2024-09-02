from fastapi import APIRouter, Depends
from typing import Annotated
from database_service.models.query_param import QueryParamsModel

router = APIRouter(prefix='/users')

@router.get('')
async def get_all(query: Annotated[QueryParamsModel, Depends(QueryParamsModel)]):
    pass

@router.get('/{id}')
async def get_one(id: str):
    pass

@router.post('')
async def create_one(id: str):
    pass

@router.patch('/{id}')
async def update_one(id: str):
    pass

@router.put('/{id}')
async def update_file(id: str):
    pass

@router.delete('/{id}')
async def delete_one(id: str):
    pass