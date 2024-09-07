from abc import ABC, abstractmethod

class DatabaseServiceABC(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def create_metadata(self):
        pass

    @staticmethod
    @abstractmethod
    def get_instance() -> "DatabaseServiceABC":
        pass

    @abstractmethod
    def getOne(self, id: str, schema):
        pass

    @abstractmethod
    def getAll(self, query, schema):
        pass

    @abstractmethod
    def createOne(self, data: dict, schema):
        pass

    @abstractmethod
    def updateOne(self, id: str, data: dict, schema):
        pass
    
    @abstractmethod
    def deleteOne(self, id: str, schema):
        pass