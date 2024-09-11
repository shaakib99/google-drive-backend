from file_service.aws_provider import AWSProvider
from file_service.lib.abcs.provider_abc import FileProviderABC

class FileUploadService:
    def __init__(self, file_upload_provider: FileProviderABC = AWSProvider()) -> None:
        self.file_upload_provider = file_upload_provider
    
    def upload(self, file: bytes):
        pass

    def upload_multiple(self, files: list[bytes]):
        pass