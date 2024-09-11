from pydantic import BaseModel
from datetime import datetime

class FileModel(BaseModel):
    id: int
    url: str
    provider: str
    mimetype: str
    is_deleted: bool
    created_date: datetime

    class Config:
        from_attribute = True
        orm_mode = True