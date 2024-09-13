from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    id: int
    name: str
    email: str
    password: Optional[str] = None
    profile_picture:  Optional[str] = None
    password_reset_token:  Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True
        orm_mode = True
