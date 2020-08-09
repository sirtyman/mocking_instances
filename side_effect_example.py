from unittest.mock import Mock


my_mock = Mock(side_effect=[1, 2, 3, 4])

print(my_mock())
print(my_mock())
print(my_mock())
print(my_mock())


args_map = {'a': 'a', 'b': 'b', 'c': 'c'}


def my_side_effect(arg):
    return args_map[arg]


my_mock = Mock(side_effect=my_side_effect)
print(my_mock('b'))
print(my_mock('c'))
print(my_mock('a'))


my_mock = Mock(side_effect=RuntimeError('Uuups...runtime error'))
my_mock()
