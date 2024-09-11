from file_service.lib.abcs.provider_abc import FileProviderABC

class LocalStorageProvider(FileProviderABC):
    def __init__(self) -> None:
        pass

    def upload(self, file: bytes):
        pass

    def upload_multiple(self, files: list[bytes]):
        pass