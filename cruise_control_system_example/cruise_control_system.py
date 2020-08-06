class CruiseControlSystem:
    def __init__(self):
        self.expected_speed = None

    def set_expected_speed(self, value):
        self.expected_speed = value

    def control(self, speed_sensor, engine):
        if speed_sensor.current() == 0:
            raise RuntimeError('Car is stopped. Cannot set the speed')
        elif speed_sensor.current() < self.expected_speed:
            engine.speed_up()
        elif speed_sensor.current() > self.expected_speed:
            engine.slow_down()