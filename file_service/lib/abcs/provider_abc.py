from abc import ABC, abstractmethod
from fastapi import UploadFile
from file_service.models.file_model import FileModel

class FileProviderABC(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def upload(self, file: UploadFile) -> FileModel:
        pass

    @abstractmethod
    async def upload_multiple(self, files: list[UploadFile]) -> list[FileModel]:
        pass