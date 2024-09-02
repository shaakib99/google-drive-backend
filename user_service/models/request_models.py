from pydantic import BaseModel, Field

class CreateUserModel(BaseModel):
    name: str = Field(min_length=2, max_length=255, pattern='[a-zA-Z]')
    email: str = Field(pattern='')
    password: str = Field(min_length= 8, max_length= 32, pattern='')

class UpdateUserModel(BaseModel):
    name: str = Field(min_length=2, max_length=255, pattern='[a-zA-Z]')
    password: str = Field(min_length= 8, max_length= 32, pattern='')
