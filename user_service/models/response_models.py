from pydantic import BaseModel

class UserResponseModel(BaseModel):
    name: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True
        orm_mode = True