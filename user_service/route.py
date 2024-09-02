from fastapi import APIRouter

router = APIRouter(prefix='/users')

@router.get('')
async def get_all(query):
    pass

@router.get('/{id}')
async def get_one(id: str):
    pass

@router.post('')
async def create_one(id: str):
    pass

@router.patch('/{id}')
async def update_user(id: str):
    pass

@router.put('/{id}')
async def update_user_files(id: str):
    pass

@router.delete('/{id}')
async def delete_user(id: str):
    pass