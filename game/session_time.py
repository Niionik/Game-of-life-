import pygame

class SessionTimer:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.is_paused = False

    def get_elapsed_time(self):
        if self.is_paused:
            return self.paused_time
        return (pygame.time.get_ticks() - self.start_time) // 1000

    def pause(self):
        if not self.is_paused:
            self.paused_time = self.get_elapsed_time()
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            self.start_time = pygame.time.get_ticks() - self.paused_time * 1000
            self.is_paused = False

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.is_paused = False 