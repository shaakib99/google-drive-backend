from file_service.aws_provider import AWSProvider
from file_service.lib.abcs.provider_abc import FileProviderABC
from file_service.schemas.file_schema import FileSchema
from file_service.models.file_model import FileModel
from database_service.service import DatabaseService
from fastapi import UploadFile

class FileUploadService:
    def __init__(self, file_upload_provider: FileProviderABC = AWSProvider(), database_service = DatabaseService(FileSchema)) -> None:
        self.file_upload_provider = file_upload_provider
        self.database_service = database_service
    
    async def upload(self, file: UploadFile) -> FileSchema:
        res = await self.file_upload_provider.upload(file)
        return await self.save_file(res)

    async def upload_multiple(self, files: list[UploadFile]) -> list[FileSchema]:
        uploaded_files = await self.file_upload_provider.upload_multiple(files)
        res = []
        for file in uploaded_files:
            saved_file = await self.save_file(file)
            res.append(saved_file)
        return res
    
    async def save_file(self, data: FileModel):
        return self.database_service.createOne(data.model_dump())