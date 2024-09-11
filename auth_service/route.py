from fastapi import APIRouter, Depends, Request
from auth_service.models.auth_models import LoginModel, GenerateResetPasswordTokenModel, ResetPasswordModel
from auth_service.service import AuthService
from common.interceptors.use_interceptor import UseInterceptor
from common.interceptors.email_interceptor import EmailInterceptor
from common.models.dependencies_model import CommonDependenciesModel
from common.utils import inject_common_dependencies
from typing import Annotated

router = APIRouter(prefix='/users')



@router.post('/login', status_code=200)
async def login(
    data: LoginModel, 
    auth_service: Annotated[AuthService, Depends(lambda: AuthService())]):
    return await auth_service.login(data)

@router.post('/generate-reset-password-token')
@UseInterceptor(EmailInterceptor())
async def generate_reset_password_token(
    data: GenerateResetPasswordTokenModel, 
    auth_service: Annotated[AuthService, Depends(lambda: AuthService())],
    dependencies: Annotated[CommonDependenciesModel, Depends(inject_common_dependencies)]
    ):
    return await auth_service.generate_password_reset_token(data)

@router.put('/reset-password')
async def reset_password(
    data: Annotated[ResetPasswordModel, Depends(ResetPasswordModel)], 
    auth_service: Annotated[AuthService, Depends(lambda: AuthService())]):
    return await auth_service.reset_password(data)