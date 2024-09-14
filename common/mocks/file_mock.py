import pytest
from file_service.models.file_model import FileModel
from datetime import datetime

@pytest.fixture
def file_model_data():
    return FileModel(id = 1, url='test.txt', mimetype='image/png', provider='LOCAL', is_deleted=False, created_date=datetime.now())