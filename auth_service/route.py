from fastapi import APIRouter, Depends
from auth_service.models.auth_models import LoginModel, GenerateResetPasswordTokenModel, ResetPasswordModel
from auth_service.service import AuthService
from typing import Annotated

router = APIRouter(prefix='/users')

@router.post('/login', status_code=200)
async def login(
    data: LoginModel, 
    auth_service: Annotated[AuthService, Depends(lambda: AuthService())]):
    return await auth_service.login(data)

@router.post('/generate-reset-password-token')
async def generate_reset_password_token(
    data: Annotated[GenerateResetPasswordTokenModel, Depends(GenerateResetPasswordTokenModel)], 
    auth_service: Annotated[AuthService, Depends(lambda: AuthService())]):
    return await auth_service.generate_password_reset_token(data)

@router.put('/reset-password')
async def reset_password(
    data: Annotated[ResetPasswordModel, Depends(ResetPasswordModel)], 
    auth_service: Annotated[AuthService, Depends(lambda: AuthService())]):
    return await auth_service.reset_password(data)