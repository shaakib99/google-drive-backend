from file_service.models.response_model import FileResponseModel
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserResponseModel(BaseModel):
    name: str
    email: str
    profile_picture: Optional[FileResponseModel] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True