from pydantic import BaseModel

class QueryParamsModel(BaseModel):
    limit: int = 10
    skip: int = 0
    selected_fields: list[str] = []
    join_fields: list[str] = []
    filter_by: str = None
    group_by: str = None
    order_by: str = None
    having: str = None
