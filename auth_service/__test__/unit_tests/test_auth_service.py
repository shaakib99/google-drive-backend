from unittest.mock import patch, MagicMock
from user_service.schemas.user_schema import UserSchema
from common.mocks.user_mock import user_model_data
from common.exceptions import NotFoundException, BadRequestException
from auth_service.service import AuthService
from auth_service.models.auth_models import LoginModel, ResetPasswordModel, GenerateResetPasswordTokenModel
import pytest
from datetime import datetime, timedelta

@pytest.mark.asyncio
@patch('database_service.service.DatabaseService')
async def test_login(mock_database_service, user_model_data):
    mock_database_service_instance = mock_database_service(UserSchema)
    auth_service = AuthService(mock_database_service_instance)

    login_model = LoginModel(email='test@email.com', password='test1234')
    # mock expected result
    mock_database_service_instance.getAll.return_value = []

    try:
        await auth_service.login(login_model)
    except Exception as e:
        assert isinstance(e, NotFoundException), 'Should not be able to find user'
    
    mock_database_service_instance.getAll.return_value = [user_model_data]
    result = await auth_service.login(login_model)
    
    assert result.id is not None, 'Should have found the user'

@pytest.mark.asyncio
@patch('database_service.service.DatabaseService')
async def test_reset_password(mock_database_service, user_model_data):
    mock_database_service_instance = mock_database_service(UserSchema)
    auth_service = AuthService(mock_database_service_instance)

    reset_password_model = ResetPasswordModel(new_password='test213213', token='2143245325325rtfg32')

    # mock expected result
    mock_database_service_instance.getAll.return_value = []

    try:
        await auth_service.reset_password(reset_password_model)
    except Exception as e:
        assert isinstance(e, NotFoundException), 'Should not be able to find user'

    
    # mock expected result
    user_model_data.password_reset_token_generated_at = datetime.now() - timedelta(minutes=40)
    mock_database_service_instance.getAll.return_value = [user_model_data]
    mock_database_service_instance.updateOne.return_value = user_model_data

    try:
        await auth_service.reset_password(reset_password_model)
    except Exception as e:
        assert isinstance(e, BadRequestException), 'Should throw token expire error'

    
    # mock expected result
    user_model_data.password_reset_token_generated_at = datetime.now()
    mock_database_service_instance.getAll.return_value = [user_model_data]
    mock_database_service_instance.updateOne.return_value = user_model_data

    result = await auth_service.reset_password(reset_password_model)

    assert result.id is not None, 'Should have found the user'

@pytest.mark.asyncio
@patch('database_service.service.DatabaseService')
async def test_generate_reset_password_token(mock_database_service, user_model_data):
    mock_database_service_instance = mock_database_service(UserSchema)
    auth_service = AuthService(mock_database_service_instance)

    reset_password_model = GenerateResetPasswordTokenModel(email='test@email.com')

    # mock expected result
    mock_database_service_instance.getAll.return_value = []

    try:
        await auth_service.generate_password_reset_token(reset_password_model)
    except Exception as e:
        assert isinstance(e, NotFoundException), 'Should not be able to find user'

    
    # mock expected result
    mock_database_service_instance.getAll.return_value = [user_model_data]
    mock_database_service_instance.updateOne.return_value = user_model_data

    result = await auth_service.generate_password_reset_token(reset_password_model)

    assert result.id is not None, 'Should have updated password_reset_token'

    