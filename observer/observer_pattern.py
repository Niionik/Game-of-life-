from abc import ABC, abstractmethod
import pygame
import random

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# Concrete observer class
class Circle(Observer):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, subject):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Subject class
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.observers = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.notify()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Observer Design Pattern with Pygame")

    running = True
    clock = pygame.time.Clock()

    # Instance of our Publisher
    rectangle = Rectangle(400, 300, 50, 50, (255, 255, 255))

    # Three instances of our subscriber/observer classes.
    circles = [
        Circle(100, 100, 25, (255, 0, 0)),
        Circle(400, 200, 25, (0, 255, 0)),
        Circle(500, 300, 25, (0, 0, 255)),
    ]

    # Add the three circles as our Subscribers to the Rectangle class 
    for circle in circles:
        rectangle.attach(circle)

    # Start the game loop
    while running:
        # refresh and clear the screen with black background
        screen.fill((0, 0, 0))

        # listen for any in-game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw the rectangle at its current position
        rectangle.draw(screen)

        # draw each of the circles
        for circle in circles:
            circle.draw(screen)

        # get the current mouse position/location
        mouse_pos = pygame.mouse.get_pos()

        # check if the mouse button is pressed
        if pygame.mouse.get_pressed()[0]:
            rectangle.move(*mouse_pos) # drag the rectangle

        # display the screen buffer (i.e., screen contents)
        pygame.display.flip()
        # generate 60 frames per second
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
