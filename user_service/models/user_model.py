from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    id: int
    name: str
    email: str
    password: Optional[str] = None
    profile_picture_id:  Optional[int] = None
    profile_picture:  Optional[str] = None
    password_reset_token:  Optional[str] = None
    password_reset_token_generated_at:  Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: bool

    class Config:
        from_attributes = True
        orm_mode = True
