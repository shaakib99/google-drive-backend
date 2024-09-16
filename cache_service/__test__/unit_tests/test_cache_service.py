from unittest.mock import patch, MagicMock
from cache_service.service import CacheService
import pytest

@patch('cache_service.redis_cache_service.RedisCacheService')
@patch('cache_service.redis_cache_service.Redis')
def test_cache_service_get(mock_redis_cache_service, mock_redis):
    # mock redis package
    mock_redis.from_url.return_value = {}

    mock_redis_cache_service_instance = mock_redis_cache_service()
    mock_redis_cache_service.get_instance.return_value = mock_redis_cache_service_instance


    cache_service = CacheService(mock_redis_cache_service)

    # set expected result
    data_map = {}
    mock_redis_cache_service_instance.get = MagicMock(side_effect = lambda key: data_map.get(key))
    mock_redis_cache_service_instance.set = MagicMock(side_effect = lambda key, value: data_map.__setitem__(key, value))
    # mock_redis_cache_service_instance.exists = MagicMock(side_effect = lambda key: key in data_map)
    # mock_redis_cache_service_instance.connection.delete = MagicMock(side_effect = lambda key: data_map.__delitem__(key))
    # mock_redis_cache_service_instance.connect.return_value = None 
    # mock_redis_cache_service_instance.disconnect.return_value = None


    result = cache_service.get('test')
    assert result is None, 'Should return None'

    cache_service.set('test', {'test': 'test'})

    result = cache_service.get('test')
    assert result is not None, 'Should set data'


@patch('cache_service.redis_cache_service.RedisCacheService')
@patch('cache_service.redis_cache_service.Redis')
def test_cache_service_set(mock_redis_cache_service, mock_redis):
    # mock redis package
    mock_redis.from_url.return_value = {}

    mock_redis_cache_service_instance = mock_redis_cache_service()
    mock_redis_cache_service.get_instance.return_value = mock_redis_cache_service_instance


    cache_service = CacheService(mock_redis_cache_service)

    # set expected result
    data_map = {}

    mock_redis_cache_service_instance.get = MagicMock(side_effect = lambda key: data_map.get(key))
    mock_redis_cache_service_instance.set = MagicMock(side_effect = lambda key, value: data_map.__setitem__(key, value))
    # mock_redis_cache_service_instance.connection.delete = MagicMock(side_effect = lambda key: data_map.__delitem__(key))
    # mock_redis_cache_service_instance.connect.return_value = None 
    # mock_redis_cache_service_instance.disconnect.return_value = None


    cache_service.set('test', {'test': 'test'})

    result = cache_service.get('test')
    assert result is not None, 'Should set data'

@patch('cache_service.redis_cache_service.RedisCacheService')
@patch('cache_service.redis_cache_service.Redis')
def test_cache_service_set(mock_redis_cache_service, mock_redis):
    # mock redis package
    mock_redis.from_url.return_value = {}

    mock_redis_cache_service_instance = mock_redis_cache_service()
    mock_redis_cache_service.get_instance.return_value = mock_redis_cache_service_instance


    cache_service = CacheService(mock_redis_cache_service)

    # set expected result
    data_map = {}

    mock_redis_cache_service_instance.get = MagicMock(side_effect = lambda key: data_map.get(key))
    mock_redis_cache_service_instance.delete = MagicMock(side_effect = lambda key: data_map.__delitem__(key))
    mock_redis_cache_service_instance.set = MagicMock(side_effect = lambda key, value: data_map.__setitem__(key, value))
    # mock_redis_cache_service_instance.connect.return_value = None 
    # mock_redis_cache_service_instance.disconnect.return_value = None


    cache_service.set('test', {'test': 'test'})
    result = cache_service.get('test')
    assert result is not None, 'Should set data'

    cache_service.delete('test')

    result = cache_service.get('test')
    assert result is None, 'Should delete data'