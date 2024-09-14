from unittest.mock import MagicMock, patch
from file_service.service import FileUploadService
from file_service.schemas.file_schema import FileSchema
from common.mocks.file_mock import file_model_data
import pytest
import os
import asyncio

@pytest.mark.asyncio
@patch('file_service.local_storage_provider.LocalStorageProvider')
@patch('database_service.service.DatabaseService')
async def test_upload_and_multiple_upload(local_storage_provider_mock, database_service_mock, file_model_data):
    local_storage_provider_mock_instance = local_storage_provider_mock()
    database_service_mock_instasnce = database_service_mock(FileSchema)

    file_service = FileUploadService(local_storage_provider_mock_instance, database_service_mock_instasnce)

    # mock expected result
    mock_file_model_data = asyncio.Future()
    mock_file_model_data.set_result(file_model_data)
    local_storage_provider_mock_instance.upload.return_value =  mock_file_model_data
    database_service_mock_instasnce.createOne.return_value = await mock_file_model_data

    with open('./test.png', 'wb') as f:
        result = await file_service.upload(f)
        assert result != None, 'file should be uploaded and save'
    
    os.remove('./test.png')

    # mock result
    mock_multiple_file_model_data = asyncio.Future()
    mock_multiple_file_model_data.set_result([file_model_data])
    local_storage_provider_mock_instance.upload_multiple.return_value = mock_multiple_file_model_data

    with open('./test.png', 'wb') as f:
        result = await file_service.upload_multiple([f])
        assert len(result) == 1, 'only 1 file should be uploaded and save'
    
    os.remove('./test.png')
