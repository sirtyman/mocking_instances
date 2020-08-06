"""Stub - A simple implementation of the object on which the tested object depends.
Stub provides pre-defined behavior to the object being tested.​
"""


class SpeedSensorStub:
    def __init__(self, speed):
        self.speed = speed

    def current(self):
        return self.speed
