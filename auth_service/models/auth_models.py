from pydantic import BaseModel, Field
from user_service.models.request_models import password_requirements

class LoginModel(BaseModel):
    email: str
    password: str

class GenerateResetPasswordTokenModel(BaseModel):
    email: str

class ResetPasswordModel(BaseModel):
    token: str
    new_password: str = password_requirements