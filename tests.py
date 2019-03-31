import classes
import unittest

from unittest.mock import Mock


class AppTest(unittest.TestCase):
    def setUp(self):
        self.bar = classes.Bar()
        self.foo_instance_mock = Mock()

    def test_1(self):
        expected_return_value = "Success"
        self.set_foo_expected_return_value(expected_return_value)

        result = self.bar.bar()

        self.assertEqual(result, expected_return_value)

    def test_2(self):
        expected_return_value = "Failure"
        self.set_foo_expected_return_value(expected_return_value)

        result = self.bar.bar()

        self.assertEqual(result, expected_return_value)

    def set_foo_expected_return_value(self, expected_return_value=None):
        self.foo_instance_mock.foo = Mock(return_value=expected_return_value)
        classes.Foo = Mock(return_value=self.foo_instance_mock)
