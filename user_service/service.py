from database_service.mysql_service import MySQLService
from database_service.lib.abcs.database_service_abc import DatabaseServiceABC
from sqlalchemy.orm import DeclarativeBase
from database_service.models.query_param import QueryParamsModel

class DatabaseService:
    def __init__(self, schema: DeclarativeBase,  db: DatabaseServiceABC = MySQLService.get_instance()):
        self.db = db
        self.schema = schema
    
    def connect(self):
        self.db.connect()
    
    def disconnect(self):
        self.db.disconnect()
    
    def getOne(self, id: str):
        return self.db.getOne(id, self.schema)

    def getAll(self, query: QueryParamsModel):
        return self.db.getAll(query, self.schema)
    
    def updateOne(self, id: str, data: dict):
        return self.db.updateOne(id, data, self.schema)
    
    def deleteOne(self, id: str):
        return self.db.deleteOne(id, self.schema)
