"""Objects that have the required arguments, but do nothing. Sometimes the object being tested has some dependencies
that are not important from the current test point of view.​
"""


from cruise_control_system_example.engine import Engine


class EngineDummy(Engine):
    def speed_up(self):
        pass

    def slow_down(self):
        pass