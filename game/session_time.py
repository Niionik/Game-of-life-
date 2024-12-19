import pygame

class SessionTimer:
    def __init__(self, interval):
        self.interval = interval
        self.last_update_time = pygame.time.get_ticks()

    def should_update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.interval:
            self.last_update_time = current_time
            return True
        return False 