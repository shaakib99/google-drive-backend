from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FileModel(BaseModel):
    id: Optional[int] = None
    url: str
    provider: str
    mimetype: str
    is_deleted: Optional[bool] = None
    created_date: Optional[datetime] = None

    class Config:
        from_attribute = True
        orm_mode = True