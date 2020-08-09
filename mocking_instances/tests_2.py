from unittest import TestCase
from unittest.mock import MagicMock, patch

from mocking_instances.classes import Foo, Bar


class TestFooBar(TestCase):
    def setUp(self):
        self.addCleanup(patch.stopall)
        self.foo_inst = MagicMock()
        self.foo_inst.foo = MagicMock(return_value='Pass')
        self.foo_class_mock = patch('mocking_instances.classes.Foo', return_value=self.foo_inst).start()

    def test_001(self):
        bar = Bar()
        bar.bar()

        self.foo_inst.foo.assert_called_once()
