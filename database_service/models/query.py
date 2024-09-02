from pydantic import BaseModel

class QueryParamsModel(BaseModel):
    limit: int = 10
    skip: int = 0
    filter_by: str = None
    group_by: str = None
    aggregate: str = None

