from pydantic import BaseModel, datetime

class UserResponseModel(BaseModel):
    name: str
    email: str
    profile_picture: str = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True