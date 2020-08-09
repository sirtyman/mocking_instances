import traceback
from unittest.mock import Mock, call


mock = Mock()
mock.some_method()

mock.some_method.assert_called()
mock.some_method.assert_called_once()


mock.some_method()
try:
    mock.some_method.assert_called_once()
except AssertionError:
    print(traceback.format_exc())


mock = Mock()
mock(5)
mock(6)
mock(7)

mock.assert_has_calls([call(5), call(6), call(7)])

try:
    mock.assert_has_calls([call(5), call(7), call(6)])
except AssertionError:
    print(traceback.format_exc())

try:
    mock.assert_has_calls([call(5), call(7), call(10)], any_order=True)
except AssertionError:
    print(traceback.format_exc())
