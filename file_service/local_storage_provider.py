from file_service.lib.abcs.provider_abc import FileProviderABC
from file_service.models.file_model import FileModel
from fastapi import UploadFile
from common.utils import generate_random_characters
import random
import string
import os

class LocalStorageProvider(FileProviderABC):
    def __init__(self) -> None:
        pass

    async def upload(self, file: UploadFile, dir = '/files/') -> FileModel:
        file_name_initial = generate_random_characters(15)
        file_ext = file.filename.split('.')[-1]
        file_dir = f'{dir}{file_name_initial}.{file_ext}'

        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(file_dir, 'w+') as f:
            byte_format = await file.read()
            f.write(byte_format.decode('utf-8'))
        
        return FileModel(url=file_dir, mimetype=file.content_type, provider='LOCAL')
        

    async def upload_multiple(self, files: list[UploadFile]) -> list[FileModel]:
        res = []
        for file in files:
            f = await self.upload(file)
            res.append(f)
        return res