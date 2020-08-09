from unittest.mock import Mock


mock = Mock()
mock(1)
mock(5)

print(mock.call_count)
