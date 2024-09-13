from unittest.mock import MagicMock, patch
from user_service.service import UsersService
from user_service.schemas.user_schema import UserSchema
from common.mocks.user_mock import create_user_model, user_model_data, update_user_model
from common.exceptions import NotFoundException
from database_service.models.query_param import QueryParamsModel

@patch('database_service.service.DatabaseService')
def test_users_create(database_service_mock, create_user_model, user_model_data):
    database_service_mock_instance = database_service_mock(UserSchema)
    
    # set up expected result
    database_service_mock_instance.createOne.return_value = user_model_data

    users_service = UsersService(database_service_mock_instance)

    result = users_service.createOne(create_user_model)

    assert result != None, 'should have user data'



@patch('database_service.service.DatabaseService')
def test_user_getOne(database_service_mock, user_model_data):
    database_service_mock_instance = database_service_mock(UserSchema)
    users_service = UsersService(database_service_mock_instance)
    
    # case: user not found 
    # set up expected result
    database_service_mock_instance.getOne.return_value = None

    try:
        users_service.getOne(1)
    except Exception as e:
        assert isinstance(e, NotFoundException), 'must raise not found exception when there is no user in database'
    
    # case: user found
    # set up expected result
    database_service_mock_instance.getOne.return_value = user_model_data
    result = users_service.getOne(1)

    assert result != None, 'should have user data'



@patch('database_service.service.DatabaseService')
def test_user_UpdateOne(database_service_mock, user_model_data, update_user_model):
    database_service_mock_instance = database_service_mock(UserSchema)
    users_service = UsersService(database_service_mock_instance)
    
    # case: user not found 
    # set up expected result
    database_service_mock_instance.getOne.return_value = None

    try:
        users_service.updateOne(1, update_user_model)
    except Exception as e:
        assert isinstance(e, NotFoundException), 'must raise not found exception when there is no user in database'
    
    # case: user found
    # set up expected result
    database_service_mock_instance.getOne.return_value = user_model_data
    database_service_mock_instance.updateOne.return_value = user_model_data
    result = users_service.updateOne(1, update_user_model)

    assert result != None, 'should have updated user data'

@patch('database_service.service.DatabaseService')
def test_user_DeleteOne(database_service_mock, user_model_data):
    database_service_mock_instance = database_service_mock(UserSchema)
    users_service = UsersService(database_service_mock_instance)
    
    # case: user not found 
    # set up expected result
    database_service_mock_instance.getOne.return_value = None

    try:
        users_service.deleteOne(1)
    except Exception as e:
        assert isinstance(e, NotFoundException), 'must raise not found exception when there is no user in database'
    
    # case: user found
    # set up expected result
    database_service_mock_instance.getOne.return_value = user_model_data
    database_service_mock_instance.deleteOne.return_value = None

    result = users_service.deleteOne(1)

    assert result == None, 'should have deleted user data'

@patch('database_service.service.DatabaseService')
def test_user_getAll(database_service_mock, user_model_data):
    database_service_mock_instance = database_service_mock(UserSchema)
    users_service = UsersService(database_service_mock_instance)
    
    # case: no user found 
    # set up expected result
    database_service_mock_instance.getAll.return_value = []
    query_params = QueryParamsModel()

    result = users_service.getAll(query_params)
    assert len(result) == 0, 'Should not return anything if there is no data'

    # case: 1 user found 
    # set up expected result
    database_service_mock_instance.getAll.return_value = [user_model_data]
    result = users_service.getAll(query_params)
    assert len(result) == 1, 'Should return 1 data'

