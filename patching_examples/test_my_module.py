from unittest.mock import patch

from patching_examples.my_module import db_write, foo


def test_foo():
    with patch('patching_examples.my_module.db_write') as mmock_db_write:
        foo()
        mmock_db_write.assert_called_once()


@patch('patching_examples.my_module.db_write')
def test_foo_2(mmock_db_write):
    foo()
    mmock_db_write.assert_called_once()
