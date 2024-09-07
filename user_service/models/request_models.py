from pydantic import BaseModel, Field
from typing import Optional

password_requirements = Field(min_length= 8, max_length= 32, pattern='')

class CreateUserModel(BaseModel):
    name: str = Field(min_length=2, max_length=255, pattern='[a-zA-Z]')
    email: str = Field(pattern='')
    password: str = password_requirements

class UpdateUserModel(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=255, pattern='[a-zA-Z]')
    password: Optional[str] = password_requirements

