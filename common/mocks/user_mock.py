import pytest
from user_service.models.request_models import CreateUserModel, UpdateUserModel
from user_service.models.user_model import UserModel

@pytest.fixture
def create_user_model():
    return CreateUserModel(name='test', email='test@email.com', password='hello12345')

@pytest.fixture
def update_user_model():
    return UpdateUserModel(name='Test1')

@pytest.fixture
def user_model_data():
    return UserModel(id = 1, name='test', email='test@email.com', password='hello12345', is_active=True)