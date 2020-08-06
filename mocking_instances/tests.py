from mocking_instances import classes
import unittest

from unittest.mock import Mock, MagicMock, patch, DEFAULT


class AppTest(unittest.TestCase):
    def setUp(self):
        self.bar = classes.Bar()
        classes.Foo = Mock(return_value=Mock())

    @unittest.skip
    def test_1(self):
        expected_return_value = "Success"
        self.set_foo_expected_return_value(expected_return_value)

        result = self.bar.bar()

        self.assertEqual(result, expected_return_value)

    @unittest.skip
    def test_2(self):
        expected_return_value = "Failure"
        self.set_foo_expected_return_value(expected_return_value)

        result = self.bar.bar()

        self.assertEqual(result, expected_return_value)

    @unittest.skip
    @patch('classes.Foo')
    def test_3(self, FooClass):
        # inst_foo = Mock()
        # classes.Foo = Mock(return_value=inst_foo)
        # classes.Foo.return_value.foo = Mock()

        # with patch('classes.Foo') as foo_class_mock:
        #     foo_class_mock.return_value = Mock()
        #     foo_class_mock.return_value.foo = Mock()

        FooClass.return_value = Mock()
        FooClass.return_value.foo = Mock()

        bar = classes.Bar()
        bar.bar()
        # classes.Foo.return_value.foo.assert_called_once()
        FooClass.return_value.foo.assert_called_once()

    def test_4(self):
        inst_foo = Mock()
        classes.Foo = Mock(return_value=inst_foo)
        classes.Foo.return_value.foo = Mock()

        bar = classes.Bar()
        bar.bar()

        classes.Foo.return_value.foo.assert_called_once()

    def set_foo_expected_return_value(self, expected_return_value=None):
        self.foo_instance_mock.foo = Mock(return_value=expected_return_value)
        classes.Foo = Mock(return_value=self.foo_instance_mock)
