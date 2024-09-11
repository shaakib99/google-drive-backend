from pydantic import BaseModel
from datetime import datetime

class FileResponseModel(BaseModel):
    url: str
    mimetype: str
    created_date: datetime

    class Config:
        from_attribute = True
        orm_mode = True