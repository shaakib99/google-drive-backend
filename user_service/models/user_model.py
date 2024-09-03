from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    name: str
    email: str
    password: str
    profile_picture: str
    password_reset_token: str
    is_active: str

    class Config:
        from_attributes = True
        orm_mode = True
