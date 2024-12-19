class SpeedController:
    def __init__(self, interval):
        self.set_speed(interval)

    def set_speed(self, new_interval):
        if not isinstance(new_interval, int) or new_interval <= 0:
            raise ValueError("Interval must be a positive integer")
        self.interval = new_interval

    def get_speed(self):
        return self.interval 