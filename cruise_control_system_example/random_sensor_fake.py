"""Fakes are objects that have working implementations, but not same as production one.
Usually take some shortcut and have simplified version of production code.
"""
from random import randint

import cruise_control_system_example.speed_sensor as speed_sensor


class RandomSpeedSensorFake(speed_sensor.SpeedSensor):
    def __init__(self):
        pass

    def current(self):
        return randint(1, 100)