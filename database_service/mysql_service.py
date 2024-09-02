from database_service.lib.abcs.database_service_abc import DatabaseServiceABC
from database_service.models.query import QueryParamsModel
from sqlalchemy.orm import DeclarativeBase

class MySQLService(DatabaseServiceABC):
    def __init__(self) -> None:
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def getOne(self, id: str, schema: DeclarativeBase):
        pass

    def getAll(self, query: QueryParamsModel, schema: DeclarativeBase):
        pass

    def createOne(self, data: dict, schema: DeclarativeBase):
        pass

    def updateOne(self, id: str, data: dict, schema: DeclarativeBase):
        pass

    def deleteOne(self, id: str, schema: DeclarativeBase):
        pass
