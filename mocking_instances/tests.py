from mocking_instances import classes
import unittest

from unittest.mock import Mock, MagicMock, patch


class AppTest(unittest.TestCase):
    def setUp(self):
        pass

    @staticmethod
    def test_patchings_instance_methods():
        foo_inst = MagicMock()
        foo_inst.foo = MagicMock(return_value='Pass')
        with patch('mocking_instances.classes.Foo', return_value=foo_inst):
            bar = classes.Bar()
            assert bar.bar() == "Pass"

            foo_inst.foo.assert_called_once()

    @staticmethod
    def test_patchings_instance_methods_v2():
        with patch('mocking_instances.classes.Foo') as mock_foo_class:
            mock_foo_class.return_value = MagicMock(spec=['foo'])
            mock_foo_class.return_value.foo.return_value = "Pass"

            bar = classes.Bar()

            assert bar.bar() == "Pass"
            mock_foo_class.return_value.foo.assert_called_once()

