from abc import abstractmethod, ABC 

class CacheABC(ABC):

    @abstractmethod
    def connect() -> None:
        pass

    @abstractmethod
    def disconnect() -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_instance() -> "CacheABC":
        pass

    @abstractmethod
    def get(key: str) -> dict:
        pass

    @abstractmethod
    def set(key: str, data: dict) -> None:
        pass

    @abstractmethod
    def delete(key: str) -> None:
        pass
