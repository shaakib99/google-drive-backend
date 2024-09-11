from abc import ABC, abstractmethod

class FileProviderABC(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def upload(self, file: bytes):
        pass

    @abstractmethod
    async def upload_multiple(self, files: list[bytes]):
        pass