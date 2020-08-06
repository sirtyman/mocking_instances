"""The goal is not to provide specific behavior, but to provide an answer to the question of
whether the activity was performed.​"""

from cruise_control_system_example.engine import Engine


class EngineSpy(Engine):
    def __init__(self):
        self.accelerate = False
        self.slow_down = False

    def speed_up(self):
        self.accelerate = True

    def slow_down(self):
        self.slow_down = True
