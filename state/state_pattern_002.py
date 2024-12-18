from abc import ABC, abstractmethod
import pygame
import time
from enum import Enum

# Define an enumeration for the colors of the traffic light
class Color(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"

# Define the interface for the traffic light state
class TrafficLightState(ABC):
    # Define the interface method for transitioning to the next state
    abstractmethod
    def next(self, light: 'TrafficLight') -> None:
        pass

    # Define the interface method for getting the current color
    abstractmethod
    def get_color(self) -> Color:
        pass

# Define the concrete state for the green light
class GreenState(TrafficLightState):
    def next(self, light: 'TrafficLight') -> None:
        # Transition to the yellow state
        light.current_state = YellowState()

    def get_color(self) -> Color:
        # Return the green color
        return Color.GREEN

# Define the concrete state for the yellow light
class YellowState(TrafficLightState):
    def next(self, light: 'TrafficLight') -> None:
        # Transition to the red state
        light.current_state = RedState()

    def get_color(self) -> Color:
        # Return the yellow color
        return Color.YELLOW

# Define the concrete state for the red light
class RedState(TrafficLightState):
    def next(self, light: 'TrafficLight') -> None:
        # Transition to the green state
        light.current_state = GreenState()

    def get_color(self) -> Color:
        # Return the red color
        return Color.RED

# Define the context for the traffic light
class TrafficLight:
    current_state: TrafficLightState = GreenState()

    # Define the method for transitioning to the next state
    def next(self) -> None:
        self.current_state.next(self)

    # Define the method for getting the current color
    def get_color(self) -> Color:
        return self.current_state.get_color()

# Define the traffic light simulation
class TrafficLightSimulation:
    def __init__(self):
        self.light = TrafficLight()
        self.cycle = 0
        self.screen = None
        self.width = 400
        self.height = 800

    # Define the method for starting the simulation
    def start(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Traffic Light Simulation')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Transition to the next state
            self.cycle += 1
            self.light.next()

            # Draw the screen
            self.draw()
            pygame.display.update()
            time.sleep(3)

    # Define the method for stopping the simulation
    def stop(self) -> None:
        pygame.quit()

    # Define the method for drawing the screen
    def draw(self) -> None:
        # Fill the screen with light gray color
        self.screen.fill((211, 211, 211))

        red_color = (255, 0, 0)
        yellow_color = (255, 255, 0)
        green_color = (0, 255, 0)

        # Define the color of the traffic light outlines
        outline_color = (70, 70, 70)

        rect_x = self.width // 4
        rect_y = self.height // 8
        rect_width = self.width // 2
        rect_height = self.height // 1.5

        # Draw the rectangle for the traffic light fixture
        pygame.draw.rect(self.screen, outline_color, (rect_x, rect_y, rect_width, rect_height), 10)

        # Draw the outline and color of the red light
        radius = 50
        center_x = self.width // 2
        center_y = self.height // 2

        pygame.draw.circle(self.screen, outline_color, (center_x, center_y - (rect_height // 4)), radius + 5, 5)
        if self.light.get_color() == Color.RED:
            pygame.draw.circle(self.screen, red_color, (center_x, center_y - (rect_height // 4)), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y - (rect_height // 4)), radius)

        # Draw the outline and color of the yellow light
        pygame.draw.circle(self.screen, outline_color, (center_x, center_y), radius + 5, 5)
        if self.light.get_color() == Color.YELLOW:
            pygame.draw.circle(self.screen, yellow_color, (center_x, center_y), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y), radius)

        # Draw the outline and color of the green light
        pygame.draw.circle(self.screen, outline_color, (center_x, center_y + (rect_height // 4)), radius + 5, 5)
        if self.light.get_color() == Color.GREEN:
            pygame.draw.circle(self.screen, green_color, (center_x, center_y + (rect_height // 4)), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y + (rect_height // 4)), radius)

if __name__ == '__main__':
    # Create an instance of the TrafficLightSimulation class
    simulation = TrafficLightSimulation()
    
    try:
        # Start the simulation loop
        simulation.start()
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, stop the simulation
        simulation.stop()
   
