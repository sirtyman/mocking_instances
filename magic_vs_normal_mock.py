from unittest.mock import MagicMock, Mock


try:
    my_mock = Mock()
    my_mock.__str__.return_value = "Normal mock"
    print(my_mock)
except AttributeError as e:
    print(e)

try:
    my_mock = MagicMock()
    my_mock.__str__.return_value = "Normal mock"
    print(my_mock)
except AttributeError as e:
    print(e)


class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def __eq__(self, other):
        return self.capacity == other.capacity


engine = Engine(2200)
engine_v2 = Engine(2200)
print(engine == engine_v2)

engine_mock = MagicMock()
engine_mock.capacity = 2200

print(engine == engine_mock)

engine_mock.__eq__.return_value = True
print(engine_mock == engine)
