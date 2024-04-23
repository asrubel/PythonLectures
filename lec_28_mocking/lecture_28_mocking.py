# Mock
from unittest.mock import Mock

mock = Mock()
print(mock.some_attribute)
print(mock.some_method())

print(mock)

json = mock
print(json.dumps('sdfsdgfdfg'))
print(json.loads('{"key": "value"}').get('key'))

# json.loads('{"key": "value"}')
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

print(json.loads.call_count)
print(json.loads.call_args)
print(json.method_calls)
